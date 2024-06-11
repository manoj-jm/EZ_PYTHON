class Person:
  def __init__(manoj,name,gender) -> None:
    manoj.name = name
    manoj.gen = gender
  
  def walk(manoj):
    print(manoj.name , " can walk")

  def eat(manoj):
    print(manoj.name , " can eat ")

  def gender(manoj):
    print(f"{manoj.name} is a {manoj.gen}")

  def insta_followers(manoj,num):
    manoj.followers = num
    return manoj.followers
  
  def instaProfile(manoj):
    print(f"{manoj.name} has {manoj.followers} followers")

adithya = Person('adithya','male')
saket = Person('saket','male')
nikila = Person('nikila','female')
nikila.walk()
nikila.eat()
nikila.insta_followers(455)
nikila.instaProfile()



