def scaleGenerator(tonic):
    sharp=['A', 'A♯', 'B', 'C', 'C♯', 'D', 'D♯', 'E', 'F', 'F♯', 'G', 'G♯']
    flat=['A', 'B♭', 'B', 'C', 'D♭', 'D', 'E♭', 'E', 'F', 'G♭', 'G', 'A♭']

    if tonic.upper() in ['A', 'B♭', 'B', 'C', 'D♭', 'D', 'E♭', 'E', 'F', 'G♭', 'G', 'A♭']:
        raju=sharp
    else:
        raju=flat

    raju_index=raju.index(tonic.upper())
    scale=raju[raju_index:]+raju[:raju_index]
    return scale

if __name__=="__main__":
    tonic=input("enter tonic:")
    print(scaleGenerator(tonic))
