## convert data , in what structure we want the data to be converted to 

from rest_framework import serializers
from travello.models import Projects

class ProjectsSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    company_name = serializers.CharField()
    img = serializers.ImageField(use_url=True)
    desc = serializers.CharField()
    equipments_used = serializers.CharField()
    

    def create(self, data):
        return Projects.objects.create(**data)

