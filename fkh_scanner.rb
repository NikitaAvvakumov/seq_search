begin
  require 'bio'
rescue LoadError => e
  raise unless e.message =~ /bio/
  puts "This script requires the BioRuby gem. Please install it via `gem install bio`"
end

class Scanner
  include Bio
  DIVERGENT_FKH_REGEX = /T[AG]TT[TG][AG][CT].{65,80}[AG][CT][AC]AA[CT]A/
  CONVERGENT_FKH_REGEX = /[AG][CT][AC]AA[CT]A.{65,80}T[AG]TT[TG][AG][CT]/
  MELT_STRETCH = /(A{5,}|T{5,}|A{4,}.*A{4,}|T{4,}.*T{4,})/

  def initialize(file_name:, tail_length_to_trim:)
    @file = file_name
    @tail_size = tail_length_to_trim.to_i
  end

  def call
    load_data_from_file
    select_ars_sequences_from_input_data
    puts "Total ARS elements: #{@ars_sequences.size}"
    trim_tails
    find_divergent_fkh_sites
    puts "Divergent Fkh sites: #{@fkh_sequences.size}"
    find_fkh_aaa_sites
    puts "Divergent Fkh sites & A stretch: #{@fkh_aaa_sequences.size}"
    puts @fkh_aaa_sequences.map { |seq| seq.definition }
    output_final_data_to_file
  end

  private

  def load_data_from_file
    @input_data = Bio::FastaFormat.open @file
  end

  def select_ars_sequences_from_input_data
    @ars_sequences = @input_data.select do |entry|
      entry.definition.match /ARS/
    end
  end

  def trim_tails
    @ars_sequences.each do |seq|
      seq.data = seq.data.slice(@tail_size, (seq.data.size - 2 * @tail_size))
    end
  end

  def find_divergent_fkh_sites
    @fkh_sequences = @ars_sequences.select do |seq|
      # seq.seq =~ DIVERGENT_FKH_REGEX ||
      #   rev_comp(seq.seq) =~ DIVERGENT_FKH_REGEX
      seq.seq =~ CONVERGENT_FKH_REGEX ||
        rev_comp(seq.seq) =~ CONVERGENT_FKH_REGEX
    end
  end

  def find_fkh_aaa_sites
    @fkh_aaa_sequences = @fkh_sequences.select do |seq|
      fkh_and_aa_within(seq.seq) || fkh_and_aa_within(rev_comp(seq.seq))
    end
  end

  def rev_comp(seq)
    Bio::Sequence::NA.new(seq).complement
  end

  def fkh_and_aa_within(seq)
    # seq.scan(DIVERGENT_FKH_REGEX).map { |n| n.match(MELT_STRETCH) }.any?
    seq.scan(CONVERGENT_FKH_REGEX).map { |n| n.match(MELT_STRETCH) }.any?
  end

  def output_final_data_to_file
    # file = File.open('output_data/divergent_fkh_aaa_motifs_near_ars.txt', 'w')
    # file.puts "Total number of ARS-proximal divergent Fkh with internal A/T stretch: #{@fkh_aaa_sequences.size}"
    file = File.open('output_data/convergent_fkh_aaa_motifs_near_ars.txt', 'w')
    file.puts "Total number of ARS-proximal convergent Fkh with internal A/T stretch: #{@fkh_aaa_sequences.size}"
    file.puts @fkh_aaa_sequences.map { |seq| seq.definition.split(' ').first }.join(', ')
    file.close
    puts "Final data written to #{file.path}"
  end
end

unless ARGV.length == 2
  raise ArgumentError, "Run script with `ruby fkh_scanner.rb <file name> <length of sequence tails to trim>"
end
Scanner.new(file_name: ARGV[0], tail_length_to_trim: ARGV[1]).call
