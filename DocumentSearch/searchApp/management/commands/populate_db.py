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
           overview='Gaming are thrones with gangs and the man of the hsjjs',
        )
        got.save()
        got.genre.add(fantacy, horror, romance)
        got.authors.add(mike, jess)

        the_life = NovelModel.objects.create(
        title='The Life',
        overview='The life is a story of a love life between angelina and joe',
        )
        the_life.save()
        the_life.genre.add(fantacy, horror, romance)
        the_life.authors.add(johnny)

        young_sheldon = NovelModel.objects.create(
           title='Young Sheldon',
           overview='Hey !! shelly how are you doing today',
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
           overview='the vampire lord of the nightmare land. But with only a captive of the Vistani woman and an untrustworthy of the ghost for allies',
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