#This is a  ruby program that shall be used as a test for all the new things I've learned
#Intializ variables
reason = "random"
string = "123"
threewords = "I am a Rebel"

#create statements
puts "asdfghjklqwertyuiopzxcvbnm" if reason == "random"
puts "You rebel!" if (string.is_a?(Integer)) or threewords.split.length >3
# team.rb
class Team
  include Enumerable # LOTS of functionality

  attr_accessor :name, :players
  def initialize (name)
    @name = name
    @players = []
  end
  def add_players (*players) # splat
    @players += players
  end
  def to_s
    "#{@name} team: #{@players.join(", ")}"
  end
  def each
    @players.each { |player| yield player }
  end
end
