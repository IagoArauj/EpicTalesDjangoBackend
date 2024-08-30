from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import (Campaign, Note, Player)
from .serializer import (CampaignSerializer, NoteSerializer, PlayerSerializer)
from epictales.gen_pagination_links import gen_pagination_links

# Create your views here.

# Campaigns
@api_view(['GET'])
def get_paginated_campaigns(request: Request) -> Response:
    try:
        limit = int(request.GET.get('limit', 20))
        offset = int(request.GET.get('offset', 0))
    except ValueError:
        return Response({
            'error': 'Invalid limit or offset'
        }, status=status.HTTP_400_BAD_REQUEST)

    campaigns = Campaign.objects.all().order_by('-id').order_by('-status')[offset:limit+offset]
    (count, pages, next_link, prev_link) = gen_pagination_links(request, Campaign, limit, offset)
    
    for campaign in campaigns:
        campaign.description = " ".join(campaign.description.split()[:10]) + " [...]" if len(campaign.description.split()) > 10 else campaign.description
    
    return Response({
        'count': count,
        'pages': pages,
        'next_page': next_link,
        'previous_page': prev_link,
        'results': CampaignSerializer(campaigns, many=True).data
    }, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_3_ongoing_campaign(request: Request) -> Response:
    campaigns = Campaign.objects.filter(status='ONGOING').order_by('-id')[:3]
    
    for campaign in campaigns:
        campaign.description = " ".join(campaign.description.split()[:20]) + " [...]" if len(campaign.description) > 20 else campaign.description
    
    return Response(CampaignSerializer(campaigns, many=True).data, status=status.HTTP_200_OK)
    

@api_view(['POST'])
def create_campaign(request: Request) -> Response:
    campaign = CampaignSerializer(data=request.data)
    if campaign.is_valid():
        campaign.save()
        return Response(campaign.data, status=status.HTTP_201_CREATED)

    return Response(campaign.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def campaign_detail(request: Request, id: int) -> Response:
    campaign = get_object_or_404(Campaign, pk=id)
    
    if request.method == 'GET':
        return Response(CampaignSerializer(campaign).data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        campaign_serializer = CampaignSerializer(campaign, data=request.data)
        if campaign_serializer.is_valid():
            campaign_serializer.save()
            return Response(campaign_serializer.data, status=status.HTTP_200_OK)
        
        return Response(campaign_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        campaign.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
# Notes

@api_view(['GET'])
def get_paginated_notes(request: Request, campaignId) -> Response:
    try:
        limit = int(request.GET.get('limit', 20))
        offset = int(request.GET.get('offset', 0))
    except ValueError:
        return Response({
            'error': 'Invalid limit or offset'
        }, status=status.HTTP_400_BAD_REQUEST)

    notes = Note.objects.filter(campaign=campaignId).order_by('-id')[offset:limit+offset]
    (count, pages, next_link, prev_link) = gen_pagination_links(request, Note, limit, offset)
    
    return Response({
        'count': count,
        'pages': pages,
        'next_page': next_link,
        'previous_page': prev_link,
        'results': NoteSerializer(notes, many=True).data
    }, status=status.HTTP_200_OK)
    
@api_view(['POST'])
def create_note(request: Request, campaign_id: int) -> Response:
    note = NoteSerializer(data=request.data)
    
    if note.initial_data.get('campaign') != campaign_id and note.initial_data.get('campaign') is not None:
        return Response({"campaign": "Campaign ID does not match"}, status=status.HTTP_400_BAD_REQUEST)
    
    if note.initial_data.get('campaign') is None:
        note.initial_data['campaign'] = campaign_id
    
    get_object_or_404(Campaign, pk=campaign_id)
    
    if note.is_valid():
        note.save()
        return Response(note.data, status=status.HTTP_201_CREATED)

    return Response(note.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def note_detail(request: Request, campaign_id, id: int) -> Response:
    note = get_object_or_404(Note, pk=id)
    
    if request.method == 'GET':
        return Response(NoteSerializer(note).data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        note_serializer = NoteSerializer(note, data=request.data)
        if note.initial_data.get('campaign') != campaign_id:
            return Response({"campaign": "Campaign ID does not match"}, status=status.HTTP_400_BAD_REQUEST)
        
        if note.initial_data.get('campaign') is None:
            note.initial_data['campaign'] = campaign_id
        
        get_object_or_404(Campaign, pk=campaign_id)
        
        if note_serializer.is_valid():
            note_serializer.save()
            return Response(note_serializer.data, status=status.HTTP_200_OK)
        
        return Response(note_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# Players

@api_view(['GET'])
def get_players(request: Request, campaign_id: int) -> Response:
    players = Player.objects.filter(campaign=campaign_id)
    return Response(PlayerSerializer(players, many=True).data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_player(request: Request, campaign_id: int) -> Response:
    player = PlayerSerializer(data=request.data)
    
    if player.initial_data.get('campaign') != campaign_id:
        return Response({"campaign": "Campaign ID does not match"}, status=status.HTTP_400_BAD_REQUEST)
    
    if player.initial_data.get('campaign') is None:
        player.initial_data['campaign'] = campaign_id
    
    get_object_or_404(Campaign, pk=campaign_id)
    
    if player.is_valid():
        player.save()
        return Response(player.data, status=status.HTTP_201_CREATED)

    return Response(player.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def player_detail(request: Request, campaign_id: int, id: int) -> Response:
    player = get_object_or_404(Player, pk=id)
    
    if request.method == 'GET':
        return Response(PlayerSerializer(player).data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        player_serializer = PlayerSerializer(player, data=request.data)
        
        if player.initial_data.get('campaign') != campaign_id:
            return Response({"campaign": "Campaign ID does not match"}, status=status.HTTP_400_BAD_REQUEST)
        
        if player.initial_data.get('campaign') is None:
            player.initial_data['campaign'] = campaign_id
        
        get_object_or_404(Campaign, pk=campaign_id)
        if player_serializer.is_valid():
            player_serializer.save()
            return Response(player_serializer.data, status=status.HTTP_200_OK)
        
        return Response(player_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        player.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)