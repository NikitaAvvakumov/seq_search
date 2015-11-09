require 'csv'

def process_array_data
  convert_to_csv
  split_by_chromosome
  puts "Done"
end

def convert_to_csv
  puts "Converting tab-delimited data to CSV"
  CSV.foreach("input_data/GSE55155_FinalData.txt", col_sep: '\t') do |row|
    CSV.open("output_data/GSE55155_FinalData.csv", "a") do |csv|
      csv << row[0].split("\t")
    end
  end
  puts "Conversion finished"
end

def split_by_chromosome
  puts "Splitting data into files by chromosome"
  CSV.foreach("output_data/GSE55155_FinalData.csv", :headers => :first_row) do |row|
    chrom_number = row[0]
    CSV.open("output_data/GSE55155_chrom#{chrom_number}.csv", "a") do |csv|
      csv << row
    end
  end
end

process_array_data
