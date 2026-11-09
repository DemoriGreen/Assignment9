class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
    '''

    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        if friend is not self and friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''

    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name in self.people:
            print(f"Person not added. {name} is already in the network.")
            return

        self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people:
            print(f"Friendship not created. {person1_name} doesn't exist!")
            return

        if person2_name not in self.people:
            print(f"Friendship not created. {person2_name} doesn't exist!")
            return

        if person1_name == person2_name:
            print("Friendship not created. A person cannot be friends with themselves.")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]

        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        for name, person in self.people.items():
            friend_names = [friend.name for friend in person.friends]
            print(f"{name} is friends with: {', '.join(friend_names)}")


# Test your code here
if __name__ == "__main__":
    network = SocialNetwork()

    network.add_person("Alex")
    network.add_person("Jordan")
    network.add_person("Morgan")
    network.add_person("Taylor")
    network.add_person("Casey")
    network.add_person("Riley")

    network.add_friendship("Alex", "Jordan")
    network.add_friendship("Alex", "Morgan")
    network.add_friendship("Jordan", "Taylor")
    network.add_friendship("Morgan", "Casey")
    network.add_friendship("Taylor", "Riley")
    network.add_friendship("Casey", "Riley")
    network.add_friendship("Morgan", "Riley")
    network.add_friendship("Alex", "Taylor")

    network.add_friendship("Alex", "Johnny")
    network.add_person("Alex")
    network.add_friendship("Alex", "Jordan")

    network.print_network()


'''
Design Memo

A graph is the right structure for a social network because people can have
friendships with many different people, and those friendships go both ways.
Each person is a node, and each friendship is an edge. An adjacency list
works well because every Person object keeps a list of its friends. This
makes it easy to add people and connect them without needing a large table
of every possible relationship.

A regular list would not work as well because it would store people, but it
would not clearly organize who is connected to whom. Finding all of one
person's friends would require checking relationships separately. A tree
would also be a poor fit because trees usually have a parent and child
structure. Social networks do not follow that rule. One person can be
friends with many people, and those people can also be connected to each
other.

One trade-off I noticed is that checking whether a friendship already exists
takes time because the friends list must be searched. Adding a friendship
is usually quick, but it can take longer when a person has many friends.
Printing the network takes time based on the number of people and the total
number of friendships because each person's friend list must be displayed.
The adjacency list also uses memory only for friendships that actually
exist, which is helpful for a large network where not everyone knows
everyone else.
'''
