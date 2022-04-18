import re

lyrics = """
If you wanna run away with me
I know a galaxy and I can take you for a ride
I had a premonition that we fell into a rhythm
Where the music don't stop for life
Glitter in the sky, glitter in my eyes
Shining just the way I like
If you're feeling like you need a little bit of company
You met me at the perfect time

You want me, I want you, baby
My sugarboo, I'm levitating
The Milky Way, we're renegading
(Yeah, yeah, yeah, yeah, yeah)

I got you, moonlight, you're my starlight
I need you, all night
Come on, dance with me
(I'm levitating)
You, moonlight, you're my starlight
I need you, all night
Come on, dance with me
(I'm levitating)

I believe that you're for me, I feel it in our energy
I see us written in the stars
We can go wherever, so let's do it now or never
Baby, nothing's ever, ever too far
Glitter in the sky, glitter in our eyes
Shining just the way we are
I feel like we're forever, every time we get together
But whatever, let's get lost on Mars

You want me, I want you, baby
My sugarboo, I'm levitating
The Milky Way, we're renegading
(Yeah, yeah, yeah, yeah, yeah)

I got you, moonlight, you're my starlight
I need you, all night
Come on, dance with me
(I'm levitating)
You, moonlight, you're my starlight
I need you, all night
Come on, dance with me
(I'm levitating)

You can fly away with me tonight
You can fly away with me tonight
Baby, let me take you for a ride
(Yeah, yeah, yeah, yeah, yeah)
(I'm levitating)
You can fly away with me tonight
You can fly away with me tonight
Baby, let me take you for a ride
(Yeah, yeah, yeah, yeah, yeah)

My love is like a rocket, watch it blast off
And I'm feeling so electric, dance my ass off
And even if I wanted to, I can't stop
(Yeah, yeah, yeah, yeah, yeah)
My love is like a rocket, watch it blast off
And I'm feeling so electric, dance my ass off
And even if I wanted to, I can't stop
(Yeah, yeah, yeah, yeah, yeah)

You want me, I want you, baby
My sugarboo, I'm levitating
The Milky Way, we're renegading

I got you, moonlight, you're my starlight
I need you, all night
Come on, dance with me
(I'm levitating)

You can fly away with me tonight
You can fly away with me tonight
Baby, let me take you for a ride
(Yeah, yeah, yeah, yeah, yeah)
(I'm levitating)
You can fly away with me tonight
You can fly away with me tonight
Baby, let me take you for a ride
(Yeah, yeah, yeah, yeah, yeah)

I got you, moonlight, you're my starlight
I need you, all night
Come on, dance with me
(I'm levitating)
You, moonlight, you're my starlight
I need you, all night
Come on, dance with me
(I'm levitating)
"""
print(type(lyrics))


if __name__ == '__main__':
    print("Hello Ghen!") # printing to console
    print("Hello Yoch!")

    print("lyrics")
    print(lyrics) # print the variable lyrics

    count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("levitating"), lyrics))
    print(count)