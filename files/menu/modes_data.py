def modes_data(index, animatronics_ai):
    match index:
        case 1: # 20/20/20/20
            animatronics_ai["WITHERED_FREDDY"] = 20
            animatronics_ai["WITHERED_BONNIE"] = 20
            animatronics_ai["WITHERED_CHICA"] = 20
            animatronics_ai["FOXY"] = 20
            animatronics_ai["BALOON_BOY"] = 0
            animatronics_ai["TOY_FREDDY"] = 0
            animatronics_ai["TOY_BONNIE"] = 0
            animatronics_ai["TOY_CHICA"] = 0
            animatronics_ai["MANGLE"] = 0
            animatronics_ai["GOLDEN_FREDDY"] = 0
        case 2: # Double Trouble
            animatronics_ai["WITHERED_FREDDY"] = 0
            animatronics_ai["WITHERED_BONNIE"] = 20
            animatronics_ai["WITHERED_CHICA"] = 0
            animatronics_ai["FOXY"] = 5
            animatronics_ai["BALOON_BOY"] = 0
            animatronics_ai["TOY_FREDDY"] = 0
            animatronics_ai["TOY_BONNIE"] = 20
            animatronics_ai["TOY_CHICA"] = 0
            animatronics_ai["MANGLE"] = 0
            animatronics_ai["GOLDEN_FREDDY"] = 0
        case 3: # New and Shiny
            animatronics_ai["WITHERED_FREDDY"] = 0
            animatronics_ai["WITHERED_BONNIE"] = 0
            animatronics_ai["WITHERED_CHICA"] = 0
            animatronics_ai["FOXY"] = 0
            animatronics_ai["BALOON_BOY"] = 10
            animatronics_ai["TOY_FREDDY"] = 10
            animatronics_ai["TOY_BONNIE"] = 10
            animatronics_ai["TOY_CHICA"] = 10
            animatronics_ai["MANGLE"] = 10
            animatronics_ai["GOLDEN_FREDDY"] = 0
        case 4: # Night of Misfits
            animatronics_ai["WITHERED_FREDDY"] = 0
            animatronics_ai["WITHERED_BONNIE"] = 0
            animatronics_ai["WITHERED_CHICA"] = 0
            animatronics_ai["FOXY"] = 0
            animatronics_ai["BALOON_BOY"] = 20
            animatronics_ai["TOY_FREDDY"] = 0
            animatronics_ai["TOY_BONNIE"] = 0
            animatronics_ai["TOY_CHICA"] = 0
            animatronics_ai["MANGLE"] = 20
            animatronics_ai["GOLDEN_FREDDY"] = 10
        case 5: # Ladies Night
            animatronics_ai["WITHERED_FREDDY"] = 0
            animatronics_ai["WITHERED_BONNIE"] = 0
            animatronics_ai["WITHERED_CHICA"] = 20
            animatronics_ai["FOXY"] = 0
            animatronics_ai["BALOON_BOY"] = 0
            animatronics_ai["TOY_FREDDY"] = 0
            animatronics_ai["TOY_BONNIE"] = 0
            animatronics_ai["TOY_CHICA"] = 20
            animatronics_ai["MANGLE"] = 20
            animatronics_ai["GOLDEN_FREDDY"] = 0
        case 6: # Foxy Foxy
            animatronics_ai["WITHERED_FREDDY"] = 0
            animatronics_ai["WITHERED_BONNIE"] = 0
            animatronics_ai["WITHERED_CHICA"] = 0
            animatronics_ai["FOXY"] = 20
            animatronics_ai["BALOON_BOY"] = 0
            animatronics_ai["TOY_FREDDY"] = 0
            animatronics_ai["TOY_BONNIE"] = 0
            animatronics_ai["TOY_CHICA"] = 0
            animatronics_ai["MANGLE"] = 20
            animatronics_ai["GOLDEN_FREDDY"] = 0
        case 7: # Freddy's Circus
            animatronics_ai["WITHERED_FREDDY"] = 20
            animatronics_ai["WITHERED_BONNIE"] = 0
            animatronics_ai["WITHERED_CHICA"] = 0
            animatronics_ai["FOXY"] = 10
            animatronics_ai["BALOON_BOY"] = 10
            animatronics_ai["TOY_FREDDY"] = 20
            animatronics_ai["TOY_BONNIE"] = 0
            animatronics_ai["TOY_CHICA"] = 0
            animatronics_ai["MANGLE"] = 0
            animatronics_ai["GOLDEN_FREDDY"] = 10
        case 8: # Cupcake Challenge
            animatronics_ai["WITHERED_FREDDY"] = 5
            animatronics_ai["WITHERED_BONNIE"] = 5
            animatronics_ai["WITHERED_CHICA"] = 5
            animatronics_ai["FOXY"] = 5
            animatronics_ai["BALOON_BOY"] = 5
            animatronics_ai["TOY_FREDDY"] = 5
            animatronics_ai["TOY_BONNIE"] = 5
            animatronics_ai["TOY_CHICA"] = 5
            animatronics_ai["MANGLE"] = 5
            animatronics_ai["GOLDEN_FREDDY"] = 5
        case 9: # Fazbear Fever
            animatronics_ai["WITHERED_FREDDY"] = 10
            animatronics_ai["WITHERED_BONNIE"] = 10
            animatronics_ai["WITHERED_CHICA"] = 10
            animatronics_ai["FOXY"] = 10
            animatronics_ai["BALOON_BOY"] = 10
            animatronics_ai["TOY_FREDDY"] = 10
            animatronics_ai["TOY_BONNIE"] = 10
            animatronics_ai["TOY_CHICA"] = 10
            animatronics_ai["MANGLE"] = 10
            animatronics_ai["GOLDEN_FREDDY"] = 10
        case 10: # Golden Freddy
            animatronics_ai["WITHERED_FREDDY"] = 20
            animatronics_ai["WITHERED_BONNIE"] = 20
            animatronics_ai["WITHERED_CHICA"] = 20
            animatronics_ai["FOXY"] = 20
            animatronics_ai["BALOON_BOY"] = 20
            animatronics_ai["TOY_FREDDY"] = 20
            animatronics_ai["TOY_BONNIE"] = 20
            animatronics_ai["TOY_CHICA"] = 20
            animatronics_ai["MANGLE"] = 20
            animatronics_ai["GOLDEN_FREDDY"] = 20

    return animatronics_ai