import sys

# receive from stdin (piped input)
for line in sys.stdin:

    # split on whitespace
    pieces = line.split()

    # the line between the header and the data has no spaces, ignore it
    if len(pieces) < 2:
        continue

    # header has a . at the end
    if pieces[-1] == '.':
        continue

    flight = {}

    # depending on length of the input, we have a flight number or not
    if len(pieces) == 9: # no flight number
        flight["id"] = pieces[0]
        flight["altitude"] = pieces[1]
        flight["speed"] = pieces[2]
        flight["lat"] = pieces[3]
        flight["lon"] = pieces[4]
        flight["track"] = pieces[5]
        flight["messages"] = pieces[6]
        flight["seen"] = pieces[7]

    elif len(pieces) == 10: #with flight number
        flight["id"] = pieces[0]
        flight["flight"] = pieces[1]
        flight["altitude"] = pieces[2]
        flight["speed"] = pieces[3]
        flight["lat"] = pieces[4]
        flight["lon"] = pieces[5]
        flight["track"] = pieces[6]
        flight["messages"] = pieces[7]
        flight["seen"] = pieces[8]

    else:
        # skip errors
        continue

    print(f"{flight}")
