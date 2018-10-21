import json
from collections import defaultdict

authors_citations = defaultdict(list)

for i in range(input()):
    data = raw_input()
    temp = json.loads(data)
    citation_count = temp["citing_paper_count"]
    for i in temp["authors"]["authors"]:
        authors_citations[i["full_name"]].append(citation_count)

answers = defaultdict(list)

for i in authors_citations:
    values = authors_citations[i]
    values.sort()
    length = len(values)
    out = 0
    for j in range(length):
        if( length - j   >= values[j]  ):
            out = values[j]
        else:
            if(values[j] > length - j and length - j > out ):
                out = length - j
    answers[out].append(i)


temp = sorted(answers.keys())
temp = temp[::-1]

for i in temp:
    for k in sorted(answers[i]):
        print k , i


"""
10
{"authors": {"authors": [{"author_order": 1,"affiliation": "","full_name": "Echo"}, {"author_order": 2,"affiliation": "","full_name": "Bravo"}, {"author_order": 3,"affiliation": "","full_name": "Alfa"}]},"title": "Article Title 1","article_number": "1","publication_title": "Publication Title 1","publication_number": "7","citing_paper_count": 9,"publisher": "IEEE"}
{"authors": {"authors": [{"author_order": 1,"affiliation": "","full_name": "Charlie"}, {"author_order": 2,"affiliation": "","full_name": "Bravo"}]},"title": "Article Title 2","article_number": "2","publication_title": "Publication Title 1","publication_number": "7","citing_paper_count": 9,"publisher": "IEEE"}
{"authors": {"authors": [{"author_order": 1,"affiliation": "","full_name": "Echo"}, {"author_order": 2,"affiliation": "","full_name": "Delta"}, {"author_order": 3,"affiliation": "","full_name": "Alfa"}, {"author_order": 4,"affiliation": "","full_name": "Charlie"}]},"title": "Article Title 3","article_number": "3","publication_title": "Publication Title 1","publication_number": "7","citing_paper_count": 4,"publisher": "IEEE"}
{"authors": {"authors": [{"author_order": 1,"affiliation": "","full_name": "Charlie"}]},"title": "Article Title 4","article_number": "4","publication_title": "Publication Title 1","publication_number": "7","citing_paper_count": 9,"publisher": "IEEE"}
{"authors": {"authors": [{"author_order": 1,"affiliation": "","full_name": "Charlie"}, {"author_order": 2,"affiliation": "","full_name": "Echo"}, {"author_order": 3,"affiliation": "","full_name": "Alfa"}]},"title": "Article Title 5","article_number": "5","publication_title": "Publication Title 1","publication_number": "7","citing_paper_count": 5,"publisher": "IEEE"}
{"authors": {"authors": [{"author_order": 1,"affiliation": "","full_name": "Charlie"}, {"author_order": 2,"affiliation": "","full_name": "Echo"}]},"title": "Article Title 6","article_number": "6","publication_title": "Publication Title 1","publication_number": "7","citing_paper_count": 6,"publisher": "IEEE"}
{"authors": {"authors": [{"author_order": 1,"affiliation": "","full_name": "Delta"}]},"title": "Article Title 7","article_number": "7","publication_title": "Publication Title 1","publication_number": "7","citing_paper_count": 4,"publisher": "IEEE"}
{"authors": {"authors": [{"author_order": 1,"affiliation": "","full_name": "Charlie"}]},"title": "Article Title 8","article_number": "8","publication_title": "Publication Title 1","publication_number": "7","citing_paper_count": 9,"publisher": "IEEE"}
{"authors": {"authors": [{"author_order": 1,"affiliation": "","full_name": "Delta"}, {"author_order": 2,"affiliation": "","full_name": "Charlie"}]},"title": "Article Title 9","article_number": "9","publication_title": "Publication Title 1","publication_number": "7","citing_paper_count": 4,"publisher": "IEEE"}
{"authors": {"authors": [{"author_order": 1,"affiliation": "","full_name": "Bravo"}, {"author_order": 2,"affiliation": "","full_name": "Echo"}]},"title": "Article Title 10","article_number": "10","publication_title": "Publication Title 1","publication_number": "7","citing_paper_count": 6,"publisher": "IEEE"}
"""

# Solved Completely
