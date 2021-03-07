from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
chatbot = ChatBot('Eden')
trainer = ListTrainer(chatbot)
trainer.train([
    'Hello'
    'Hi! How are you?',
'Im good',
'Thats great! Are you writing today?',
'Im ok',
'Thats good. Are you writing today?',
'Im not feeling great',
'Sorry to hear that. Tell me more.',
'Im having a tough day',
'That sucks. Im listening :)',
'Ive been writing today',
'Awesome! How did it go?',
'I got some writing done',
'Well done! How did it go?',
'I should be writing',
'Writing can be hard, its ok to take a break',
'Im a master procrastinator myself!',
'My writings awful',
'Writing is hard, and everyone hates early drafts!', 
'I cant concentrate',
'Have you tried putting some music on? I like this Spotify playlist for writing: https://open.spotify.com/playlist/4s7fvXVjb233wv4WPrNmMG?si=3e253967a9f54289',
'I feel blocked',
'Have you tried taking a break or doing a different task? Sometimes that helps me.',
'I havent done enough reading yet',
'Thats ok, you can start with what you know. Make some notes about what you have read, and then see where the gaps are. Then you can look for literature to fill those gaps.',
'This is too hard',
'Writing is hard! But you got this, I believe in you!',
'Writing is so hard',
'Youre right, it is hard! Just write one line to start with. Just one, thatll help you write the next one. And before you know it youll have written a paragraph.',
'I love writing',
'Thats so cool! I love writing too <3',
'Can you give me some writing tips?',
'Sure! Try and create a writing cue for your brain, to make it easier to switch to "writing mode". For example, put on your fave writing playlist, or make a cup of your favourite warm beverage',
'Id love to! Try and create a writing habit by writing something everyday. It doesnt matter if its not for your project, it could be writing in a journal, a blog post, or poetry. Getting into the habit of putting something down on paper makes it easier every time we "have" to sit and write.',
'Think about the structure of your writing. You might want to create an outline with bullet points, or a document with headings. It can help organise your thoughts before getting stuck into the body of the text.',
'Ask people to read your writing and give you feedback often. Ideally, ask you supervisor, but you could also ask friends, colleagues, or other PhD students you know.',
'If youre finding it consistently hard to write, to the point where it seems unusual, dont be afraid to ask for help. You could ask your supervisor, or the support department at your university.',
'That makes me feel better',
'Im glad',
'Is there anyone I can ask for advice',
'Your supervisor should always be your first port of call for something to do with your studies, but theres loads of other support available at the University. Have a look at: www.ed.ac.uk',
])
greeting = input('Type your name: ')
while True:
    request=input(greeting+": ")
    if request=='Bye' or request =='bye':
        print('Eden: Bye')
        break
    else:
        response=chatbot.get_response(request)
        print('Eden:',response)
