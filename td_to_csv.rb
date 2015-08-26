require 'csv'

CSV.foreach("GSE55155_FinalData.txt", col_sep: '\t') do |row|
  CSV.open("GSE55155_FinalData.csv", "a") do |csv|
    csv << row[0].split("\t")
  end
end
