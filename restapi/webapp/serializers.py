from rest_framework import serializers
from rest_framework import employees

class employeesSerializer(Serializers.ModelSerializer):

	class Meta:
		model= employees
		#fields= ('firstname', 'lastname')
	fields= '__all__'
