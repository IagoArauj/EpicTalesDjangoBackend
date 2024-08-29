from django.urls import path
from .views import *

urlpatterns = [
    path('', get_paginated_campaigns, name='get_paginated_campaigns'),
    path('create/', create_campaign, name='create_campaign'),
    path('<int:id>/', campaign_detail, name='campaign_detail'),
    path('<int:campaign_id>/notes/', get_paginated_notes, name='get_paginated_notes'),
    path('<int:campaign_id>/notes/create/', create_note, name='create_note'),
    path('<int:campaign_id>/notes/<int:id>/', note_detail, name='note_detail'),
    path('<int:campaign_id>/players', get_players, name='get_players'),
    path('<int:campaign_id>/players/create/', create_player, name='create_player'),
    path('<int:campaign_id>/players/<int:id>/', player_detail, name='player_detail'),

]