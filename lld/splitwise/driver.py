# Sample Usage
<<<<<<< Updated upstream
from lld.splitwise.groups import Group
from lld.splitwise.users import User

if __name__ == "__main__":
    sheldon = User("sheldon@example.com", "sheldon")
    lenord = User("lenord@example.com", "Lenord")
    howard = User("howard@example.com", "howard")
    raj = User("raj@example.com", "raj")


    comic_con = Group("Comic Con", owner=sheldon)
    comic_con.add_member(lenord)
    comic_con.add_member(howard)
    comic_con.add_member(raj)

    # Add expenses within the group
    comic_con.add_expense(amount=150, description="Hotel Bill", payer=lenord, participants=["all"])
    comic_con.add_expense(amount=200, description="Dinner", payer=howard, participants=["all"])

    print(comic_con.get_balance_report())

    print("second expense")

    comic_con.add_expense(amount=300, description="Breakfast", payer=raj,
                               participants=[howard, lenord, raj])

    print(comic_con.get_balance_report())

    comic_con.add_expense(amount=3000, description="Gifts", payer=raj,
                          participants=["all"])

    print(comic_con.get_balance_report())
    print(f"{raj.balance}")
    print(f"{lenord.balance}")
    print(f"{raj.balance}")
    print(f"{sheldon.balance}")

    print(f"Group 2 expense")
    print("**"*5)

    bday = Group("sheldon birthday", owner=lenord)
    bday.add_member(raj)
    bday.add_member(howard)

    bday.add_expense(amount=5000, description="Gifts", payer=raj,
                          participants=["all"])

    bday.add_expense(amount=200, description="Cake", payer=raj,
                          participants=["all"])

    bday.add_expense(amount=150, description="Drinks", payer=raj,
                          participants=["all"])

    print(bday.get_balance_report())
    raj.total_balance()
    lenord.total_balance()
    howard.total_balance()
    sheldon.total_balance()


=======
# Create Users
from lld.splitwise.groups import Group
from lld.splitwise.users import User

alice = User("alice@example.com", "Alice")
bob = User("bob@example.com", "Bob")
carol = User("carol@example.com", "Carol")

# Create a Group with Alice as the owner
trip_group = Group("Trip to Vegas", owner=alice)
trip_group.add_member(bob)
trip_group.add_member(carol)

# Add an expense and split it
trip_group.add_expense(amount=150, description="Hotel Bill", payer=alice, participants=[alice, bob, carol])

# Check balances
print(f"Alice Balance: {alice.balance}")
print(f"Bob Balance: {bob.balance}")
print(f"Carol Balance: {carol.balance}")
>>>>>>> Stashed changes
