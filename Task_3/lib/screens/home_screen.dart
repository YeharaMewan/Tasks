import 'package:flutter/material.dart';
import '../models/item.dart';
import '../widgets/item_card.dart';
import 'details_screen.dart';

class HomeScreen extends StatefulWidget {
  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  // Sample data - in a real app, this would come from an API or database
  final List<Item> items = [
    Item(
      id: 1,
      title: 'Mountain View',
      description: 'A beautiful view of mountains with snow peaks and clear blue sky. The perfect destination for adventure seekers and nature lovers who want to experience the wilderness.',
      imagePath: 'assets/images/Beach_Resort.jpg',
    ),
    Item(
      id: 2,
      title: 'Beach Resort',
      description: 'A luxurious beach resort with pristine white sand and crystal clear water. Enjoy the sound of waves and beautiful sunsets while relaxing in comfortable loungers.',
      imagePath: 'assets/images/Mountain_View.jpg',
    ),
    Item(
      id: 3,
      title: 'City Skyline',
      description: 'An impressive view of the city skyline with modern architecture and busy streets. Experience the vibrant city life with numerous restaurants, shopping centers, and entertainment options.',
      imagePath: 'assets/images/City_Skyline.jpg',
    ),
    Item(
      id: 4,
      title: 'Forest Trail',
      description: 'A serene forest trail surrounded by tall trees and diverse wildlife. Perfect for hiking enthusiasts who want to connect with nature and enjoy peaceful walks among ancient trees.',
      imagePath: 'assets/images/Forest_Trail.jpg',
    ),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Color(0xfffdc800),
      appBar: AppBar(
        title: Text('Destination List',
          style: TextStyle(
            color: Colors.black,
            fontWeight: FontWeight.bold,
          ),),
        backgroundColor: Color(0xfffdc800),
      ),
      body: ListView.builder(
        itemCount: items.length,
        itemBuilder: (context, index) {
          return ItemCard(
            item: items[index],
            onTap: () {
              // Navigate to details screen when item is tapped
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => DetailsScreen(item: items[index]),
                ),
              );
            },
          );
        },
      ),
    );
  }
}