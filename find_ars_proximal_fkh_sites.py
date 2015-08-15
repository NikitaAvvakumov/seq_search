def find_forkhead(chromosome, fkh_consensus_seq):
    chromosome_sequence = fetch_sequence_of(chromosome)
    rev_comp_chromosome_sequence = rev_comp(chromosome_sequence)
    watson_matches = find_pattern(fkh_consensus_seq, chromosome_sequence)
    crick_matches = find_pattern(fkh_consensus_seq, rev_comp_chromosome_sequence)
    print(len(watson_matches) + len(crick_matches))
    fkh_near_acs = acs_proximal(watson_matches) + acs_proximal(crick_matches)
    print(len(fkh_near_acs))

def fetch_sequence_of(chromosome):
    all_chromosomes = intermine_query("Chromosome")

    for row in all_chromosomes.rows():
        if row["primaryIdentifier"] == chromosome:
            chromosome = row["sequence.residues"]
    return chromosome

def intermine_query(type):
    from intermine.webservice import Service
    service = Service("http://yeastmine.yeastgenome.org/yeastmine/service")

    # Get a new query on the class (table) you will be querying:
    query = service.new_query(type)

    # The view specifies the output columns
    query.add_view("primaryIdentifier", "sequence.residues")

    # Uncomment and edit the line below (the default) to select a custom sort order:
    # query.add_sort_order("Chromosome.primaryIdentifier", "ASC")

    return query

def rev_comp(sequence):
    from Bio.Seq import Seq
    from Bio.Alphabet import generic_dna
    seq = Seq(sequence, generic_dna)
    return str(seq.reverse_complement())

def find_pattern(pattern, sequence):
    import regex
    return regex.findall(pattern, sequence)

def acs_proximal(sequence_list):
    import re
    acs = '(AAC[TA]AAA[CT][GA]TAAA[AT][AT][GAT][GAT]){e<=1}'
    acs_prox = [ seq for seq in sequence_list if re.search(acs, seq) ]
    return acs_prox

find_forkhead('chrI', '(.{25}[AG]TAAA[CT]A.{72}[AG]TAAA[CT]A){e<=2}')
