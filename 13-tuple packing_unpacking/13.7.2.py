"""
Use a for loop to print out the last name, year of birth, and city for each of the people. (There are multiple ways you could 
do this. Try out some code and see what happens!)
"""



julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
claude = ("Claude", "Shannon", 1916, "A Mathematical Theory of Communication", 1948, "Mathematician", "Petoskey, Michigan")
alan = ("Alan", "Turing", 1912, "Computing machinery and intelligence", 1950, "Mathematician", "London, England")

people = [julia, claude, alan]

for i in people:
    print(i[1],i[2],i[6] )