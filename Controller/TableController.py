# This function create a table with unique key(s)
def create_table_with_unique(table, column, unique):
    # Create error variable, after each mysql query, check if it is null.
    # If not null, then return error
    error = None

    # parse the list of columns from string into array
    columns = column.split(",")

    # Parse the list of unique keys from string into array.
    # Because a unique key can be composite key with a form of '(c1,c2)',
    # so it is impossible to use the same technique as what we have done for columns.
    uniques = []
    while len(unique) > 0:
        a = 0
        # Each time, there are two cases:
        # 1. The next key is a single key;
        # 2. The next key is a composite key.
        # We need to handle these two cases separately.
        comma = -1
        prent = -1
        try:
            comma = unique.index(',')
        except Exception as e:
            comma = -1
        try:
            prent = unique.index('(')
        except Exception as e:
            prent = -1

        # When the next key is a composite key...
        if comma > prent >= 0:
            end = unique.index(')')
            prent += 1
            composite_key = unique[prent: end-1]
            uniques.append(composite_key)
            unique = uniques[end+1:-1]
        # When the next key is a single key...
        else:
            if comma == 0:
                # If there is an empty key, then skip it.
                unique = unique[1:-1]
            else:
                # Cut the single key off from the tring and push it into the array.
                single_key = unique[0:comma]
                uniques.append(single_key)
                if comma == -1:
                    # If this is the last key, then empty the string.
                    unique = ""
                else:
                    unique = unique[comma+1:-1]


