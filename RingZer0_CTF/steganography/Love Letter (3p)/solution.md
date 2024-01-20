# Love Letter

## Challenge Details 

- **CTF:** RingZer0
- **Category:** Steganography
- **Points:** 3

## Provided Materials

- Piece of text:

	I went†to the park today,†saw†a lot of†fish. Fish are†cool,†but they aren't my†favorite animal!! The monkey is a†good animal,†so is the Blue-Tounged†Skink,†but†I rarely get†to see†those†at the†park! All of†this†makes me sad,†but†just encourages†me†to travel more. I'll†start researching where in†the†world I†can†see these animals†in†their natural habitat†and†start visiting them! Sounds†like†a good†time,†I'll†update here with†my†plans. It might be a long†while†though, because I†get†so busy with†work†and never have time†to†do the†actual†things I want†to†do! Oh to be†me,†and to never go out for working.†Well,†at least†the†people†at my company†are†nice! Working there is fun, and I†do†get to do some things with friends†through†work, but I still wish I could†make†friends†with those monkeys†and skinks! Well,†I†guess it's†offical: I†shall travel! Not†just†the rant†from†this blog post, but†an†actual thing I will†do. Well,†I'll†show you guys†all†the pictures anways. Did†you†know that†a monkey†is either going†to†be a Cercopithecoid†or a Platyrrhyne?? It's†true!†and their†are†264†species of monkey†that†are known.†Sure†is a lot†of†them! But skinks†are†also cool, there†are†over 1200 different†species of†skink! Skins are†lizards,†but†they look more†like snakes with†legs†to†me! But I guess since†skinks†have a tail†and†snakes don't... Oh†I†don't know! I love†animals†of all kinds,†can't†even†pick favorites. I'm†sorry fish,†you†guys are good animals†too.†ha ha, alright,†I'll†stop my†ranting.

	--End†journal entry


## Solution

By analyzing the text we can notice, that there are normal spaces and some strange symbols, so we can traverse the text and if we find space, we will interpret it as `0` and if fe find this strange symbol, we will interpret it as `1`:

```python
# Initialize an empty string to hold the binary representation
binary = ""

# Open the file in binary read mode
with open("./file.txt", "rb") as file:
    # Read the file byte by byte
    for byte in file.read():
        # Check if the byte value is 128 or greater (not ASCII)
        if byte >= 128:
            binary += "1" 
        # Check if the byte is a space character
        elif chr(byte) == ' ':
            binary += "0"

# Function to convert a binary string to text
def binary_to_text(binary_str):
    text = "" 
    # Process each 8-bit chunk of the binary string
    for i in range(0, len(binary_str), 8):
        byte = binary_str[i:i+8]  # Extract an 8-bit chunk
        text += chr(int(byte, 2))  # Convert the chunk to an integer, then to a character, and append it to the text
    return text  # Return the resulting text

# Convert the binary string to text and print it
print(binary_to_text(binary))
```

## Final Flag

`FLAG-3b6f70fcf070009561f5276fe98fc9c6`

*Created by [bu19akov](https://github.com/bu19akov)*

