def create_stats_message(strength, wisdom, dexterity):
    total = strength + wisdom + dexterity
    msg = f"You have {strength} strength, {wisdom} wisdom, and {dexterity} dexterity for a total of {total} stats."
    return msg


print(create_stats_message(5, 3, 4))

# The broken version has a mismatched indent and a missing closing quote:
#
# def create_stats_message(strength, wisdom, dexterity):
#       total = strength + wisdom + dexterity    <-- 6 spaces
#     msg = f"You have ... {total} stats.        <-- 4 spaces, and no closing "
#     return msg
#
# Python can't read it at all, so you get an error before anything runs.
# Read the stack trace from the last line up: IndentationError: unindent does not match any outer indentation level
