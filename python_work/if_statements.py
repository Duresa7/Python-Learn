# if: run the indented code only when the condition is True
def show_status(boss_health):
    if boss_health > 0:
        print("Ganondorf is alive!")
        return
    print("Ganondorf is unalive!")


show_status(10)  # Ganondorf is alive!
show_status(0)   # Ganondorf is unalive!


# Code after the if block (not indented) runs either way
def print_status(player_health):
    if player_health <= 0:
        print("dead")
    print("status check complete")


print_status(0)   # dead, then status check complete
print_status(10)  # status check complete


# if / elif / else: only the first True branch runs
def player_status(health):
    if health <= 0:
        return "dead"
    elif health <= 5:
        return "injured"
    else:
        return "healthy"


print(player_status(0))   # dead
print(player_status(3))   # injured
print(player_status(20))  # healthy


# else works without any elif
def check_high_score(current_player_name, high_scoring_player_name):
    if current_player_name == high_scoring_player_name:
        return "You are the highest scoring player!"
    else:
        return "You are not the highest scoring player!"


print(check_high_score("Ed", "Ed"))   # You are the highest scoring player!
print(check_high_score("Al", "Ed"))   # You are not the highest scoring player!


# Several elifs are fine too
def check_score_rank(player_name, high_scoring_player_name, low_scoring_player_name):
    if player_name == high_scoring_player_name:
        return "high"
    elif player_name == low_scoring_player_name:
        return "low"
    else:
        return "neither"


print(check_score_rank("Ed", "Ed", "Al"))   # high
print(check_score_rank("Al", "Ed", "Al"))   # low
print(check_score_rank("Win", "Ed", "Al"))  # neither
