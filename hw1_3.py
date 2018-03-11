def compare_subjects_within_student(math,
                                    history):
    """
    Compare the two subjects with their students and print out the "preferred"
    subject for each student. Single-subject students shouldn't be printed.

    Choice for the data structure of the function's arguments is up to you.
    
    Both arguments should be dictionaries
    """
    pref_subj={}
    for k,v in math.items():
        if k in history:
            if max(v)>max(history.get(k)):
                pref_subj[k]='Math'
            else:
                pref_subj[k]='History'
    return pref_subj


history={'Ayam': [90,95], 'Yuval': [90,95], 'Keren': [80, 85], 'Dana': [90, 100]}
math={'Ayam': [100,95], 'Yuval': [100,95], 'Keren': [80, 82], 'Dana': [90, 99], 'Rodi':[100,100]}         

print(compare_subjects_within_student(math,history))


