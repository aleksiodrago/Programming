def sorting():
    x = raw_input('What is your name?')
    if len(x) <= 5:
        print 'You,',x,', have been sorted into Huffelpuff.'
        return 'Congradulations, you have been sorted!'

    elif len(x) == 6:
        print 'You,',x,', have been sorted into Gryffindor.'
        return 'Congradulations, you have been sorted!'

    elif len(x) == 8:
        print 'You,',x,', have been sorted into Gryffindor.'
        return 'Congradulations, you have been sorted!'

    elif len(x) == 7:
        print 'You,',x,', have been sorted into Ravenclaw.'
        return 'Congradulations, you have been sorted!'

    else:
        print 'You,',x,', have been sorted into Slytherin.'
        return 'Congradulations, you have been sorted!'
sorting()
print 'Congradulations, you have been sorted!'