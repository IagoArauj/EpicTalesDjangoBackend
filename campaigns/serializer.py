from rest_framework import serializers
from campaigns.models import Campaign, Note, Player


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'
class CampaignSerializer(serializers.ModelSerializer):
    notes = NoteSerializer(many=True, read_only=True)
    class Meta:
        model = Campaign
        fields = '__all__'