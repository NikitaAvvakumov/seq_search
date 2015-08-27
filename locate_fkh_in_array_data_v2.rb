require 'csv'

FKH_PATTERNS = {
  "1" => ["600", nil, nil, nil],
  "2" => [nil, "700", nil, nil],
  "3" => [nil, nil, "800", nil],
  "4" => [nil, nil, nil, "900"]
}

LAZY_CONVERTER = {
  1 => 'I',
  2 => 'II',
  3 => 'III',
  4 => 'IV',
  5 => 'V',
  6 => 'VI',
  7 => 'VII',
  8 => 'VIII',
  9 => 'IX',
  10 => 'X',
  11 => 'XI',
  12 => 'XII',
  13 => 'XIII',
  14 => 'XIV',
  15 => 'XV',
  16 => 'XVI'
}

def locate_coords_in_array_data
  (1..16).each do |chromosome|
    puts "Processing chromosome #{chromosome}"
    fkh_sites = read_fkh_coords_from_file_for(chromosome)
    mark_locations(fkh_sites, chromosome)
  end
  puts "Done"
end

def read_fkh_coords_from_file_for(chromosome)
  chrom_id = LAZY_CONVERTER[chromosome]
  CSV.read("chr#{chrom_id}_fkh_motifs.csv").sort { |a, b| a[1].to_i <=> b[1].to_i }
end

def mark_locations(fkh_sites, chromosome)
  CSV.foreach("GSE55155_chrom#{chromosome}.csv") do |array_data|
    array_coord = array_data[1].to_i
    match = false
    fkh_sites.each do |fkh_site|
      coord = fkh_site[1].to_i
      pattern = fkh_site[2]
      if (array_coord - 25) < coord && (array_coord + 25) >= coord
        match = true
        CSV.open("fkh_chrom#{chromosome}.csv", "a") do |csv|
          csv << array_data + FKH_PATTERNS[pattern]
        end
      end
    end

    unless match
      CSV.open("fkh_chrom#{chromosome}.csv", "a") do |csv|
        csv << array_data
      end
    end
  end
end

locate_coords_in_array_data
