import 'package:flutter_test/flutter_test.dart';
import 'package:taller_datos_abiertos/models/department_model.dart';
import 'package:taller_datos_abiertos/models/president_model.dart';
import 'package:taller_datos_abiertos/models/touristic_attraction_model.dart';
import 'package:taller_datos_abiertos/models/typical_dish_model.dart';

void main() {
  group('Models Unit Tests', () {
    test('Department fromJson and toJson', () {
      final json = {
        'id': 1,
        'name': 'Amazonas',
        'description': 'Departamento del sur de Colombia',
        'cityCapitalId': 1,
        'municipalities': 2,
        'surface': 109665,
        'population': 76589,
        'phonePrefix': '8',
        'cityCapital': {
          'id': 1,
          'name': 'Leticia',
          'description': 'Capital de Amazonas',
          'surface': 5968,
          'population': 42280,
          'postalCode': '910001',
        },
      };

      final dep = Department.fromJson(json);
      expect(dep.id, 1);
      expect(dep.name, 'Amazonas');
      expect(dep.cityCapital?.name, 'Leticia');
      expect(dep.toJson()['name'], 'Amazonas');
    });

    test('President fromJson and helpers', () {
      final json = {
        'id': 1,
        'name': 'Rafael',
        'lastName': 'Núñez',
        'startPeriodDate': '1887-06-04',
        'endPeriodDate': '1888-08-07',
        'politicalParty': 'Partido Nacional',
        'description': 'Presidente histórico',
      };

      final pres = President.fromJson(json);
      expect(pres.fullName, 'Rafael Núñez');
      expect(pres.periodDisplay, '1887 – 1888');
      expect(pres.politicalParty, 'Partido Nacional');
    });

    test('TouristicAttraction fromJson', () {
      final json = {
        'id': 10,
        'name': 'Museo del Oro',
        'description': 'Museo arqueológico en Bogotá',
        'images': ['https://example.com/oro.jpg'],
        'latitude': '4.6018',
        'longitude': '-74.0721',
        'city': {'id': 1, 'name': 'Bogotá'},
      };

      final attraction = TouristicAttraction.fromJson(json);
      expect(attraction.name, 'Museo del Oro');
      expect(attraction.primaryImage, 'https://example.com/oro.jpg');
      expect(attraction.city?.name, 'Bogotá');
    });

    test('TypicalDish fromJson and ingredientsList', () {
      final json = {
        'id': 1,
        'name': 'Bandeja Paisa',
        'description': 'Plato típico antioqueño',
        'ingredients': 'Frijoles, Arroz, Huevo, Chicharrón, Arepa, Aguacate',
        'department': {'id': 2, 'name': 'Antioquia'},
      };

      final dish = TypicalDish.fromJson(json);
      expect(dish.name, 'Bandeja Paisa');
      expect(dish.ingredientsList.length, 6);
      expect(dish.ingredientsList.first, 'Frijoles');
      expect(dish.department?.name, 'Antioquia');
    });
  });
}
