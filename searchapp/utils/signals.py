from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django_elasticsearch_dsl.registries import registry

from searchapp.models import NovelModel

@receiver(post_save, sender=NovelModel)
def update_novel_document(sender, instance, **kwargs):
    registry.update(instance)



@receiver(post_delete, sender=NovelModel)
def delete_document(sender, instance, **kwargs):
    registry.delete(instance, raise_on_error=False)