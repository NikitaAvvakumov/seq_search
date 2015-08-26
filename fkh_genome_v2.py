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
    watson_starts = [match.start() for match in watson_matches]
    crick_starts = [match.start() for match in crick_matches]
    all_starts = list(set(watson_starts + crick_starts))
    all_starts.sort()
    print("Pattern {} matches: {}".format(pattern["name"],all_starts))

    file_name = "{}_fkh_motifs.csv".format(chrom_ident)
    if len(all_starts) > 0:
        with open(file_name, 'a') as f:
            for position in all_starts:
                f.write("{}, {}, {}\n".format(chrom_ident, position, pattern["name"]))

# fkh_pattern_1 = '(T[AG]TTTA[CT].{70,74}[AG]TAAA[CT]A)'
# fkh_pattern_2 = '(T[AG]TTTA[CT].{70,74}T[AG]TTTA[CT])'
# fkh_pattern_3 = '([AG]TAAA[CT]A.{70,74}T[AG]TTTA[CT])'
# fkh_pattern_4 = '([AG]TAAA[CT]A.{70,74}[AG]TAAA[CT]A)'
fkh_pattern_1 = { "name": "1", "pattern": '(T[AG]TT[TG][AG][CT].{70,74}[AG][CT][AC]AA[CT]A)' }
fkh_pattern_2 = { "name": "2", "pattern": '(T[AG]TT[TG][AG][CT].{70,74}T[AG]TT[TG][AG][CT])' }
fkh_pattern_3 = { "name": "3", "pattern": '([AG][CT][AC]AA[CT]A.{70,74}T[AG]TT[TG][AG][CT])' }
fkh_pattern_4 = { "name": "4", "pattern": '([AG][CT][AC]AA[CT]A.{70,74}[AG][CT][AC]AA[CT]A)' }

find_forkhead('chrI', fkh_pattern_1)
find_forkhead('chrI', fkh_pattern_2)
find_forkhead('chrI', fkh_pattern_3)
find_forkhead('chrI', fkh_pattern_4)
# find_forkhead('chrII', fkh_pattern_1)
# find_forkhead('chrIII', fkh_pattern_1)
# find_forkhead('chrIV', fkh_pattern_1)
# find_forkhead('chrV', fkh_pattern_1)
# find_forkhead('chrVI', fkh_pattern_1)
# find_forkhead('chrVII', fkh_pattern_1)
# find_forkhead('chrVIII', fkh_pattern_1)
# find_forkhead('chrIX', fkh_pattern_1)
# find_forkhead('chrX', fkh_pattern_1)
# find_forkhead('chrXI', fkh_pattern_1)
# find_forkhead('chrXII', fkh_pattern_1)
# find_forkhead('chrXII', fkh_pattern_1)
# find_forkhead('chrXIII', fkh_pattern_1)
# find_forkhead('chrXIV', fkh_pattern_1)
# find_forkhead('chrXV', fkh_pattern_1)
# find_forkhead('chrXVI', fkh_pattern_1)
#
# find_forkhead('chrI', fkh_pattern_allan)
# find_forkhead('chrII', fkh_pattern_allan)
# find_forkhead('chrIII', fkh_pattern_allan)
# find_forkhead('chrIV', fkh_pattern_allan)
# find_forkhead('chrV', fkh_pattern_allan)
# find_forkhead('chrVI', fkh_pattern_allan)
# find_forkhead('chrVII', fkh_pattern_allan)
# find_forkhead('chrVIII', fkh_pattern_allan)
# find_forkhead('chrIX', fkh_pattern_allan)
# find_forkhead('chrX', fkh_pattern_allan)
# find_forkhead('chrXI', fkh_pattern_allan)
# find_forkhead('chrXII', fkh_pattern_allan)
# find_forkhead('chrXII', fkh_pattern_allan)
# find_forkhead('chrXIII', fkh_pattern_allan)
# find_forkhead('chrXIV', fkh_pattern_allan)
# find_forkhead('chrXV', fkh_pattern_allan)
# find_forkhead('chrXVI', fkh_pattern_allan)
