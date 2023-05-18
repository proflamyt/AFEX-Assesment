from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from searchapp.models import Genre, NovelModel, ChapterModel

from dotenv import load_dotenv
from os import getenv, path

# Build paths inside the project like this: BASE_DIR / 'subdir'.

load_dotenv("/etc/secrets/.env")


class Command(BaseCommand):
    help = 'Populates the database with some testing data.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Started database population process...'))

        if User.objects.filter(username="test_user").exists():
            self.stdout.write(self.style.SUCCESS('Database has already been populated. Cancelling the operation.'))
            return
        
        # Create admin
        User.objects.create_superuser(
                username= getenv('admin_user'),
                password= getenv('admin_pass')
            )
        


        # Create users
        mike = User.objects.create_user(username='author1', password='really_strong_password123')
        mike.first_name = 'test'
        mike.last_name = 'afex user'
        mike.save()

        jess = User.objects.create_user(username='author2', password='really_strong_password123')
        jess.first_name = 'Jess'
        jess.last_name = 'Brown'
        jess.save()

        johnny = User.objects.create_user(username='author3', password='really_strong_password123')
        johnny.first_name = 'Johnny'
        johnny.last_name = 'Davis'
        johnny.save()

        # Create genres
        fantacy = Genre.objects.create(name='fantacy')
        horror = Genre.objects.create(name='horror')
        romance = Genre.objects.create(name='romance')

    
        # Create novels
        got = NovelModel.objects.create(
           title='Game of Throne',
           overview="""A Game of Thrones takes place on the fictional continent of Westeros, which experiences years-long seasons of varying intensity. The majority of Westeros comprises the Seven Kingdoms, and a monumental wall of ice separates the northernmost portion of the continent from the frigid wasteland beyond. In the Prologue, a group of men from the Night’s Watch—the ancient but derelict organization that guards the Wall—track a group of “wildling” people who live beyond the boundaries of the realm. Pale, blue-eyed wights kill most of their party.
            After the longest summer ever recorded, King Robert Baratheon travels north to the castle of Winterfell to see his old friend, Lord Ned Stark. About 15 years earlier, Ned helped Robert overthrow the previous king, Aerys II Targaryen. Before Robert’s arrival, Ned executes the only surviving member of the Night’s Watch party who encountered the wights for desertion; his story is considered outlandish. However, Jon Snow (the son of Ned, who wasn't married to Jon's mother when Jon was born) sees the man’s fear. After, a group of direwolf puppies is discovered in the woods. Each of the five Stark children is given a direwolf puppy to raise. Direwolves are the sigil of House Stark.

       Robert arrives after the news that his and Ned’s mutual father figure, Lord Jon Arryn, is dead. Arryn was the Hand of the King, the king’s most powerful advisor. Now, Robert wants Ned to fill the position. Ned does not trust Robert’s wife, Queen Cersei, who is part of the infamous Lannister family. Her twin brother Ser Jaime is a member of the Kingsguard, and her younger brother Tyrion is mockingly referred to as “the Imp” as he has dwarfism. Catelyn, Ned’s wife, urges Ned to accept the role. She is worried about the ulterior motives of the Lannisters and concerned about the offense Ned may cause if he declines. While the royal retinue is in Winterfell, Ned’s young son Bran spots Cersei and Jaime engaged in an incestuous sexual relationship while climbing the castle walls. Jaime pushes Bran from a window, and the fall paralyzes Bran and puts him in a coma.""",
        )
        got.save()
        got.genre.add(fantacy, horror, romance)
        got.authors.add(mike, jess)

        the_life = NovelModel.objects.create(
        title='The Life',
        overview="""Astronauts (Jake Gyllenhaal, Rebecca Ferguson, Ryan Reynolds) aboard the International Space Station are on the cutting edge of one of the most important discoveries in human history: the first evidence of extraterrestrial life on Mars. As members of the crew conduct their research, the rapidly evolving life-form proves far more intelligent and terrifying than anyone could have imagined.""",
        )
        the_life.save()
        the_life.genre.add(fantacy, horror, romance)
        the_life.authors.add(johnny)

        young_sheldon = NovelModel.objects.create(
           title='Young Sheldon',
           overview="""
           When Sheldon walks in to a near-empty classroom on his first day in High School, he sees music teacher Ms Fenley playing the opening melody of Mozart's Sonata No.11 in A K.331 on the Cello. She is, correctly, playing it in the key of A, but for some reason does not play the last note (B) of the fourth bar to end the phrase. Sheldon, as yet unseen by the teacher, sits down at the piano and plays the melody along with the teacher as she repeats the same tune, and he also leaves off the last B. She asks him if he knows the sonata, and he replies that he doesn't play piano. Later, Ms Fenley tests Sheldon by playing some chords, which he then identifies without looking at the keyboard: G minor, F, E-flat, C minor. She comments that he has perfect pitch, while the test she uses is more appropriate for identifying the skill of "relative pitch". All of this, however, is overshadowed by the question of 1) how Sheldon could immediately choose the right key on which to start the Sonata melody, and 2) how he would know the names of the chords without prior musical study.
           """,
        )
        young_sheldon.save()
        young_sheldon.genre.add(fantacy, horror, romance)
        young_sheldon.authors.add(mike)


        knight_of_roses = NovelModel.objects.create(
           title='Knight of Black roses',
           overview='On the fabled world of Krynn, Lord Soth finally learns that there is a price to pay for his long history of evil deeds, a price even an undead warrior might find horrifying.',
        )
        knight_of_roses.save()
        knight_of_roses.genre.add(fantacy, horror, romance)
        knight_of_roses.authors.add(johnny)


        the_journey = NovelModel.objects.create(
           title='The Journey',
           overview='the vampire lord of the nightmare land. But with only a captive of the Vistani woman and an untrustworthy of the ghost for allies, walking of the dead. trying to escape the grasp of the death. hello again',
        )
        the_journey.save()
        the_journey.genre.add(fantacy, horror, romance)
        the_journey.authors.add(johnny)

        # Create chapters
        ChapterModel.objects.create(
            title='Chapter 1',
            book=got,
            content='namkakmakk' 
        )

        ChapterModel.objects.create(
            title='Chapter 2',
            book=got,
            content='namkakmakk  bcjbsjhcb sbjscbj jbnsjkcnjks' 
        )

        ChapterModel.objects.create(
            title='Chapter 3',
            book=got,
            content='namkakmakk hbhb  bcjbsjhcb sbjscbj jbnsjkcnjks' 
        )
        ChapterModel.objects.create(
            title='Chapter 1',
            book=young_sheldon,
            content='namkakmakk' 
        )

        ChapterModel.objects.create(
            title='Chapter 2',
            book=young_sheldon,
            content='namkakmakk  bcjbsjhcb sbjscbj jbnsjkcnjks' 
        )

        ChapterModel.objects.create(
            title='Chapter 3',
            book=knight_of_roses,
            content='namkakmakk hbhb  bcjbsjhcb sbjscbj jbnsjkcnjks' 
        )

        ChapterModel.objects.create(
            title='Chapter 1',
            book=the_life,
            content='namkakmakknjmnjnjnj nk kkkk' 
        )

        ChapterModel.objects.create(
            title='Chapter 1',
            book=the_journey,
            content='namkakmakknjmnjnjnj' 
        )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database.'))