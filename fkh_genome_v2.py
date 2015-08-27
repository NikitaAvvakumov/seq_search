def find_forkhead(chrom_ident, pattern):
    from intermine.webservice import Service
    service = Service("http://yeastmine.yeastgenome.org/yeastmine/service")

    # Get a new query on the class (table) you will be querying:
    query = service.new_query("Chromosome")

    # The view specifies the output columns
    query.add_view("primaryIdentifier", "sequence.residues")

    # Uncomment and edit the line below (the default) to select a custom sort order:
    # query.add_sort_order("Chromosome.primaryIdentifier", "ASC")

    query.add_constraint("Chromosome.primaryIdentifier", "=", chrom_ident)

    # Return one result and raise error if there is more than one
    query.one()

    chromosome = ''
    for row in query.rows():
        chromosome = row["sequence.residues"]

    def rev_comp(dna):
        comp = ''
        for nucl in dna:
            if nucl == 'A':
                comp = comp + 'T'
            elif nucl == 'T':
                comp = comp + 'A'
            elif nucl == 'C':
                comp = comp + 'G'
            elif nucl == 'G':
                comp = comp + 'C'
            else:
                print('Not a DNA sequence')

        rev_comp = comp[::-1]
        return rev_comp

    chromosome_rev = rev_comp(chromosome)

    import regex
    watson_matches = regex.finditer(pattern["pattern"], chromosome)
    crick_matches = regex.finditer(pattern["pattern"], chromosome_rev)
    all_matches = [match.group(0) for match in watson_matches]
    all_matches += [rev_comp(match.group(0)) for match in crick_matches]
    all_matches = list(set(all_matches))

    fkh_motif_coords = []
    for match in all_matches:
        matches = regex.finditer(match, chromosome)
        match_starts = [match.start() for match in matches]
        fkh_motif_coords += match_starts

    fkh_motif_coords.sort()
    print("Pattern {} matches: {}".format(pattern["name"], fkh_motif_coords))
    file_name = "{}_fkh_motifs.csv".format(chrom_ident)

    if len(fkh_motif_coords) > 0:
        with open(file_name, 'a') as f:
            for position in fkh_motif_coords:
                f.write("{},{},{}\n".format(chrom_ident, position, pattern["name"]))

fkh_patterns = [
        { "name": "1", "pattern": '(T[AG]TT[TG][AG][CT].{70,74}[AG][CT][AC]AA[CT]A)' },
        { "name": "2", "pattern": '(T[AG]TT[TG][AG][CT].{70,74}T[AG]TT[TG][AG][CT])' },
        { "name": "3", "pattern": '([AG][CT][AC]AA[CT]A.{70,74}T[AG]TT[TG][AG][CT])' }
        ]

chromosomes = "I II III IV V VI VII VIII IX X XI XII XIII XIV XV XVI".split()
for chromosome in chromosomes:
    print("Chromosome {}:".format(chromosome))
    chr_id = "chr{}".format(chromosome)
    for pattern in fkh_patterns:
        find_forkhead(chr_id, pattern)
