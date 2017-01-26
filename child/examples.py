from child.Child import Child

def get_examples():
    children = {}
    case_properties_Bob = {'Child looks at other children playing {}': True,
                           'Child can follow something with eyes{}': True,
                           'Child changes facial expression in reaction to mad/friendly voices {}': True,
                           'Child can say a child rhyme{}': False, 'Child helps with simple domestic work {}': False,
                           'Child can jump{}': False, 'Child keeps to the rules of a game under guidance{}': False,
                           'Child can say goodbye to parents without crying{}': False,
                           'Child can talk about experiences {}': False, 'Child plays simple functional games {}': True,
                           'Child plays with ball by pushing it back {}': True,
                           'Child makes choices if asked {}': False, 'Child can laugh out loud {}': True,
                           'Child does simple domestic work tasks{}': False,
                           'Child can imitate two-word-sentences {}': False, 'Child imitates domestic work {}': True,
                           'age_full_date': '04-07-2015', 'Child can staple 2 blocks {}': True,
                           'Child can walk with support{}': True, 'Child can point to specific object {}': True,
                           'age': 18, 'Child looks shortly at face {}': True, 'Child reacts to own name {}': True,
                           'Child vocalizes in different ways {}': True, 'Child can staple 10 blocks{}': False,
                           'Child reacts in (semi) words to simple questions  {}': False,
                           'Child can look at image for 2 minutes {}': True,
                           'Child can use sounds to take its turn {}': True,
                           "Child can make at least 4 different sounds' {}": True, 'Child sit without support{}': True,
                           'Child says half of the time please and thankyou without reminder{}': False,
                           'Child uses consistent words for leaving/arriving/greeting and is able to describe movements with >2words {}': False,
                           'Child can draw a circle{}': False,
                           "Child uses words for persons, objects, animals and 'no' {}": False,
                           'Child plays 15-20min alone without adult {}': True, 'Child brabbles {}': True,
                           'Child uses adult intonation pattern including questions and exclamations  {}': False,
                           'Can speak {} words': 3, 'Child smiles at familiar game {}': True,
                           'Child can share attention of parents{}': False, 'Child looks at face for a while {}': True,
                           'Child can vocalize? {}': True, 'Child expects to be lifted by i.e. moving limbs {}': True,
                           'Child smiles if piece of cloth is put on head {}': True,
                           'Child can use 3 word-sentences {}': False, 'Child can vocalize without crying? {}': True,
                           'Child can whisper and scream {}': False,
                           'Child tries to grab piece of toy outside arm reach{}': True,
                           'Child answers during story simple questions {}': False,
                           'Child can sit without support{}': True, "Child's posture is symmetrical{}": True,
                           'Child smiles and vocalizes when meeting a faimliar person {}': True,
                           "Child often throws with toy if it doesn't want it {}": True,
                           'Child can imitate face movements in combination with sounds {}': True,
                           'Child says please if reminded {}': False,
                           'Child vocalizes interactively and makes use of voice inflections as well as objects during interaction {}': True,
                           'Child knows own gender and can name it{}': False,
                           'Child smiles or makes noice after talking {}': True,
                           'Child listens to 1 talking person in noisy environment {}': True,
                           'Child plays with hands and clothes{}': True, 'Child smiles spontaneously {}': True,
                           'Child turns image/book with correct side up to itself {}': True,
                           'Child joins with playing kiekeboe {}': True,
                           "Child asks w'questions like where, what {}": False,
                           'Child helps with putting on simple clothes {}': True,
                           'Child tries to sing along with songs {}': False,
                           'Child screams for attention and protests if by loud noise or crying something  happens that he/she dislikes {}': True,
                           'Child joins with songs/rhymes{}': False, 'Child listens to music/story for 10min {}': False,
                           'Child plays in meaningful manner {}': True, 'Child recognizes drinking bottle {}': True,
                           'Child tries to imitate adults {}': True, 'Child plays simple games together {}': True,
                           'Child can use 2 different vowels? {}': True, "Child's head balance is stable{}": True,
                           'Child uses consistent same sounds for leaving/arriving {}': False,
                           'Child plays with feet {}': True, 'Child can turn pages {}': True,
                           'Child can say its full name {}': False, 'Child plays with dolls {}': False,
                           'Child can walk without support{}': True, 'Child can sing simple songs {}': False,
                           'Child can make fist {}': True, 'Child uses adult-like intonation {}': False,
                           'Child smiles at mirror image{}': True, 'Child stays within clear rules of parents{}': False,
                           'Child reacts at noise {}': False, 'Child is quiet after picking up {}': True,
                           'Child makes soft noise upon talking {}': True, 'Child can use one vowel {}': True,
                           'Child shows toy to adult {}': True, 'Child can repeat a 6 word sentence {}': False,
                           'Child searches with eyes where sound is coming from {}': True,
                           'Child reacts with body movements upon talking {}': True, 'Child can raise head{}': True,
                           'Child can stand with support{}': True, 'Child can imitate movements and sounds {}': True,
                           'Child takes turn in conversations {}': False, 'Child avoids danger{}': False,
                           'Child plays next to other children and is in contact with them {}': False,
                           'Child can communicate with friends with signs {}': True,
                           'Child reacts on presence strangers by staring/crying {}': True,
                           'Child can use intonation patterns similar to adults {}': False,
                           'Child starts to understand basic grammar {}': False,
                           'Child plays with different sorts of toys for 10min {}': True,
                           'Child uses repeatable 2-syllable structures baba/dada {}': True,
                           'Child can doodle with pencil {}': True, 'Child waits for its own turn {}': False,
                           "Child's speech is understandable for at least 2/3 of time {}": False,
                           'Child sits quiet in chair and has attention for object {}': True,
                           'Child combines vowels and consonants to make ba/da structures {}': True,
                           'Child waits for its turn with other children{}': False,
                           'Can follow orders {} percent of time': 30, 'Child listens to 10-min story {}': False,
                           'Child brings toy/object to mouth {}': True, "Child tries to imitate 'talking' {}": True,
                           'Child is a good imitator and repeats words of adults {}': False,
                           'Child can use 3 different vowels? {}': True, 'Child can answer many questions{}': False,
                           'Child tries shows off to get attention of parents {}': True,
                           'Child had interest in surrounding{}': True, 'Child listens to short story {}': True,
                           'Child defends own toys {}': True, 'Child turns in movement of sound/voice {}': True,
                           'Child can move object {}': True}
    children['Bob'] = Child('Bob', case=case_properties_Bob)

    children['Lisa'] = Child('Lisa', case={'age_full_date': '24-08-2014', 'age': 29,
                                           'Child searches with eyes where sound is coming from {}': True,
                                           'Child uses repeatable 2-syllable structures baba/dada {}': True,
                                           'Child uses adult-like intonation {}': False,
                                           'Child stays within clear rules of parents{}': False,
                                           'Child can answer many questions{}': False,
                                           'Child waits for its own turn {}': False,
                                           'Child plays with different sorts of toys for 10min {}': True,
                                           'Can speak {} words': 40, 'Child is quiet after picking up {}': True,
                                           'Child can sing simple songs {}': False,
                                           'Child helps with simple domestic work {}': False,
                                           'Child plays simple games together {}': True,
                                           'Child takes turn in conversations {}': True,
                                           'Child can staple 10 blocks{}': True,
                                           'Child says please if reminded {}': False,
                                           'Child plays with hands and clothes{}': True,
                                           'Child can use 3 word-sentences {}': True,
                                           'Child makes soft noise upon talking {}': True,
                                           'Child can use intonation patterns similar to adults {}': True,
                                           'Child expects to be lifted by i.e. moving limbs {}': True,
                                           'Child smiles spontaneously {}': True,
                                           'Child can stand with support{}': True,
                                           'Child can imitate face movements in combination with sounds {}': True,
                                           'Child can say goodbye to parents without crying{}': False,
                                           "Child can make at least 4 different sounds' {}": True,
                                           'Child sit without support{}': True,
                                           "Child often throws with toy if it doesn't want it {}": True,
                                           'Child can move object {}': True, 'Child can vocalize? {}': True,
                                           'Child brings toy/object to mouth {}': True,
                                           'Child knows own gender and can name it{}': False,
                                           'Child plays with feet {}': True, 'Can follow orders {} percent of time': 40,
                                           'Child plays in meaningful manner {}': True,
                                           'Child says half of the time please and thankyou without reminder{}': False,
                                           'Child turns image/book with correct side up to itself {}': True,
                                           "Child asks w'questions like where, what {}": True,
                                           'Child plays with ball by pushing it back {}': True,
                                           'Child tries to grab piece of toy outside arm reach{}': True,
                                           'Child can walk without support{}': True,
                                           'Child can use sounds to take its turn {}': True,
                                           'Child shows toy to adult {}': True,
                                           'Child smiles at familiar game {}': True, 'Child plays with dolls {}': False,
                                           "Child uses words for persons, objects, animals and 'no' {}": True,
                                           'Child tries to sing along with songs {}': True,
                                           'Child can say its full name {}': False,
                                           'Child plays 15-20min alone without adult {}': True,
                                           'Child can use 3 different vowels? {}': True,
                                           'Child can point to specific object {}': True,
                                           'Child looks at face for a while {}': True,
                                           'Child tries shows off to get attention of parents {}': True,
                                           'Child can follow something with eyes{}': True,
                                           'Child listens to 1 talking person in noisy environment {}': True,
                                           'Child can imitate movements and sounds {}': True,
                                           'Child can use 2 different vowels? {}': True,
                                           'Child turns in movement of sound/voice {}': True,
                                           "Child's posture is symmetrical{}": True,
                                           'Child reacts on presence strangers by staring/crying {}': True,
                                           'Child can turn pages {}': True,
                                           'Child can imitate two-word-sentences {}': True,
                                           'Child can staple 2 blocks {}': True, 'Child can jump{}': True,
                                           'Child can laugh out loud {}': True,
                                           'Child is a good imitator and repeats words of adults {}': True,
                                           'Child plays next to other children and is in contact with them {}': False,
                                           'Child can talk about experiences {}': False,
                                           'Child smiles at mirror image{}': True,
                                           'Child keeps to the rules of a game under guidance{}': False,
                                           'Child can make fist {}': True, 'Child can draw a circle{}': True,
                                           'Child defends own toys {}': True, 'Child can raise head{}': True,
                                           'Child starts to understand basic grammar {}': True,
                                           "Child's speech is understandable for at least 2/3 of time {}": True,
                                           'Child listens to short story {}': True,
                                           'Child uses consistent words for leaving/arriving/greeting and is able to describe movements with >2words {}': True,
                                           'Child joins with songs/rhymes{}': False,
                                           'Child joins with playing kiekeboe {}': True,
                                           'Child can look at image for 2 minutes {}': True,
                                           'Child waits for its turn with other children{}': False,
                                           'Child smiles and vocalizes when meeting a faimliar person {}': True,
                                           'Child smiles if piece of cloth is put on head {}': True,
                                           "Child tries to imitate 'talking' {}": True,
                                           'Child does simple domestic work tasks{}': False,
                                           'Child can communicate with friends with signs {}': True,
                                           'Child can walk with support{}': True,
                                           'Child sits quiet in chair and has attention for object {}': True,
                                           'Child reacts at noise {}': True, 'Child makes choices if asked {}': False,
                                           'Child can say a child rhyme{}': False,
                                           'Child can sit without support{}': True,
                                           'Child uses consistent same sounds for leaving/arriving {}': True,
                                           'Child can vocalize without crying? {}': True,
                                           'Child can use one vowel {}': True, 'Child can doodle with pencil {}': True,
                                           'Child avoids danger{}': False, 'Child can whisper and scream {}': False,
                                           'Child tries to imitate adults {}': True,
                                           'Child reacts to own name {}': True,
                                           'Child looks at other children playing {}': True,
                                           'Child helps with putting on simple clothes {}': True,
                                           'Child vocalizes in different ways {}': True,
                                           'Child combines vowels and consonants to make ba/da structures {}': True,
                                           'Child had interest in surrounding{}': True,
                                           'Child imitates domestic work {}': True,
                                           'Child can share attention of parents{}': False,
                                           'Child can repeat a 6 word sentence {}': False,
                                           'Child changes facial expression in reaction to mad/friendly voices {}': True,
                                           'Child reacts with body movements upon talking {}': True,
                                           'Child listens to music/story for 10min {}': False,
                                           'Child listens to 10-min story {}': True,
                                           'Child plays simple functional games {}': True,
                                           "Child's head balance is stable{}": True,
                                           'Child smiles or makes noice after talking {}': True,
                                           'Child uses adult intonation pattern including questions and exclamations  {}': False,
                                           'Child reacts in (semi) words to simple questions  {}': True,
                                           'Child looks shortly at face {}': True, 'Child brabbles {}': True,
                                           'Child recognizes drinking bottle {}': True,
                                           'Child screams for attention and protests if by loud noise or crying something  happens that he/she dislikes {}': True,
                                           'Child vocalizes interactively and makes use of voice inflections as well as objects during interaction {}': True,
                                           'Child answers during story simple questions {}': True})
    return children


def example_child(child):
    children = get_examples()
    if child in children:
        return children[child]
    else:
        print("I don't know this kid!")
        print("I know these children")
        for k in children:
            print("\t {}".format(k))

