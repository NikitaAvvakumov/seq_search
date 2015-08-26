require 'csv'

fkh_patterns = {
  "1" => ["600", nil, nil, nil],
  "2" => [nil, "700", nil, nil],
  "3" => [nil, nil, "800", nil],
  "4" => [nil, nil, nil, "900"]
}

fkh_sites = CSV.read("chrI_fkh_motifs.csv")
fkh_sites.sort! do |a, b|
  a[1].to_i <=> b[1].to_i
end

CSV.foreach("GSE55155_chrom1.csv") do |array_data|
  array_coord = array_data[1].to_i
  match = false
  fkh_sites.each do |fkh_site|
    coord = fkh_site[1].to_i
    pattern = fkh_site[2]
    if (array_coord - 25) < coord && (array_coord + 25) > coord
      match = true
      CSV.open("fkh_chrom1.csv", "a") do |csv|
        csv << array_data + fkh_patterns[pattern]
      end
    end
  end

  unless match
    CSV.open("fkh_chrom1.csv", "a") do |csv|
      csv << array_data
    end
  end
end
