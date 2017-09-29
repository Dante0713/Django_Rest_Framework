from rest_framework import serializers
from articles.models import Articles


class ArticlesSerializer(serializers.ModelSerializer):

	class Meta:
		model = Articles
		# fields = '__all__'
		fields = ('id', 'articleTitle', 'articleContent', 'articleCreatedTime')
