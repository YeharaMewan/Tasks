class Item {
  final int id;
  final String title;
  final String description; //immutable
  final String imagePath;

  Item({
    required this.id,
    required this.title,
    required this.description,
    required this.imagePath,
  });
}