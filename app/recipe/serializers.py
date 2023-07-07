from rest_framework import serializers

from app.core.models import RecipeModel


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeModel
        fields = "__all__"
        read_only_fields = ['id']


class RecipeDetailSerializer(RecipeSerializer):
    """This serializer inherits the RecipeSerializer class """

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']
