class SecretStudy:
    NORTH = {
        "message":"You leave through the secret entrance back to the library.",
        "location":9,
    }
    commands = {
        "EXAMINE DESK":"On the desk is a journal and a pen.",
        "EXAMINE CHAIR":"A wooden chair with padding.",
        "EXAMINE JOURNAL":"An open leather bound journal sitting on a desk.",
        "READ JOURNAL":"""The journal is opened to the most recent entry, dated one week ago:\n 
        'My trusted servant Manfred and I went on a hunting trip 
        today.  While we were out, we came across a rabid wolf.
        It attacked us and wounded Manfred.  Somthing strange is afoot...'""",
        "EXAMINE PEN":"A beautiful silver fountain pen.",
        "NORTH":NORTH,
        "EXIT NORTH":NORTH,
        "GO NORTH":NORTH,
    }

    intro = "\nSECRET STUDY:\nLord Spooky's private study is a spartan room containing\na writing desk and a chair."

    # TODO: ITEMS: PEN, JOURNAL (Player should be able to read at any time if taken)
    # TODO: WEREWOLF: The player cannot pick up or use the silver pen!
    # EXITS: NORTH: LIBRARY