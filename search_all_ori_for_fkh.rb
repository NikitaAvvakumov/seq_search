begin
  require 'bio'

  input_file_name, tail_length_to_trim = ARGV
  input_data = load_data_from(input_file_name)
  ars_sequences = select_ars_sequences_from(input_data)
  puts ars_sequences.first.data.size
  processesed_sequences = trim_tails(ars_sequences, tail_length_to_trim.to_i)
  puts processesed_sequences.first.data.size

  def load_data_from(file)
    Bio::FastaFormat.open(file)
  end

  def select_ars_sequences_from(data)
    data.select do |entry|
      entry.definition.match /ARS/
    end
  end

  def trim_tails(sequences, tail_size)
    sequences.each do |seq|
      seq.data = seq.data.slice(tail_size, (seq.data.size - 2 * tail_size))
    end
  end

rescue LoadError => e
  raise unless e.message =~ /bio/
  puts "This script requires the BioRuby gem. Please install it via `gem install bio`"
end
