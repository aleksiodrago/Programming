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
begin

  File.foreach( 'do_not_exist.txt' ) do |line|
    puts line.chomp
  end

rescue Exception => e
  puts e.message
  puts "Let's pretend this didn't happen..."
end
