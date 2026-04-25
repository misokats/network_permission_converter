full_dot = '●'
empty_dot = '○'

# 1,create character
def create_character(name, strength, intelligence, charisma):

    # 2,3, name is string
    if not isinstance(name, str):
        return 'The character name should be a string'

    # 4,5,name is not empty
    if name == '':
        return 'The character should have a name'

    # 6,7,length of name is not longer than 10
    if len(name) > 10:
        return 'The character name is too long'
        
    # 8,9,name doesn't contain spaces
    if ' ' in name:
        return 'The character name should not contain spaces'

    # stats
    stats = [strength, intelligence, charisma] 

    #10,11,all stats are integers
    if not all(isinstance(s, int) for s in stats):
        return 'All stats should be integers'

    #12,13,all stats are all no less than 1
    if not all(s >= 1 for s in stats):
        return 'All stats should be no less than 1'

    #14,15,All stats should be no more than 4
    if all(s >= 4 for s in stats):
        return 'All stats should be no more than 4'

    #16,17,stats should't sum to 7
    if all(sum(stats) != 7 for s in stats):
        return 'The character should start with 7 points'

    #18, format dot
    return(f"strength {full_dot*5}")
    
ren = create_character('ren',4,2,1)
print(ren)

    
