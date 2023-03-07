def person_traits(name,trait_1, trait_2 =''):
    """List a person's best traits."""
    traits = trait_1

    if trait_2: 
        traits['trait_2'] = trait_2

    return traits

best_traits = person_traits('bob', 'funny', 'loyal')
print(best_traits)



    

