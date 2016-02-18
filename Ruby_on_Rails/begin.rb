# # 3.times { puts "Hello World" }
# #
# # # this is a comment
# # puts 5 # so is this
# # 3 # and this
# #
# # p "Got it" # => Got it
# times_2=2
# times_2 *= 2 while times_2<100
# puts times_2
# def add(one, two)
#   one + two
# end
#
# def divide(one, two)
#   return "I don't think so" if two == 0
#   one / two
# end
#
# puts add(2, 2) # => 4
# puts divide(2, 0) # => I don't think so
# puts divide(12, 4) # => 3
# begin
#
#   File.foreach( 'do_not_exist.txt' ) do |line|
#     puts line.chomp
#   end
#
# rescue Exception => e
#   puts e.message
#   puts "Let's pretend this didn't happen..."
# end
some_range = 1..3
puts some_range.max # => 3
puts some_range.include? 2 # => true

puts (1...10) === 5.3 # => true
puts ('a'...'r') === "r" # => false (end-exclusive)

p ('k'..'z').to_a.sample(2) # => ["k", "w"]
# or another random array with 2 letters in range

age = 12
case age
  when 0..12 then puts "Still a baby"
  when 13..99 then puts "Teenager at heart!"
  else puts "You are getting older..."
end
