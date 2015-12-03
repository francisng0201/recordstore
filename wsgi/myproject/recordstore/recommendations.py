from .models import *
from random import sample

class Recommendations():

    def __init__(self, user):
        self.user = user
        self.owned_records = self.user.ownedrecord_set
        self.pressings = self.get_pressings()

    def get_pressings(self):
        keys = self.owned_records.values('pressing')
        pressings = []
        for value in keys:
            pressings.append(Pressing.objects.get(pk=value['pressing']))

        return pressings

    def get_similar_users(self):
        similar_users = []
        for owned in self.owned_records.all():
            shared = OwnedRecord.objects.filter(album=owned.album).exclude(owner=self.user)

            for record in shared:
                user = record.owner
                if user not in similar_users:
                    similar_users.append(user)

        return similar_users

    def find_recommendations(self):
        self.recommendations = []
        similar_users = self.get_similar_users()

        for user in similar_users:
            owned = user.ownedrecord_set.all()
            for record in owned:
                if record.pressing not in self.pressings:
                    self.recommendations.append(record.pressing) 
        return self.recommendations

    def get_recommendations(self, number=10):
        self.find_recommendations()
        sample_size = min(number, len(self.recommendations))
        return sample(self.recommendations, sample_size)
