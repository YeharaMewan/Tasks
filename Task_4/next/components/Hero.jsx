"use client"

import React from "react";
import Image from "next/image";
import Eco from "../images/Eco.jpg";
import { useRouter } from 'next/navigation';

export function Hero() {
  const router = useRouter();

  const handlePreOrder = () =>{
  router.push('/Plan')
  }

  return (
    <section className="pt-32 md:pt-40 pb-16 md:pb-24">
      <div className="container mx-auto px-4 md:px-6">
        <div className="flex flex-col md:flex-row items-center">
          <div className="md:w-1/2 mb-12 md:mb-0">
            <h1 className="text-4xl md:text-5xl font-bold text-gray-800 mb-6 leading-tight">
              Charge Your Devices <span className="text-blue-600">Sustainably</span>
            </h1>
            <p className="text-xl text-gray-600 mb-8">
              Our revolutionary wireless charging technology uses recycled materials and solar power to minimize environmental impact while maximizing charging efficiency.
            </p>
            <div className="flex flex-col sm:flex-row gap-4">
              <button
                onClick={handlePreOrder}
                className="bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-8 rounded-lg shadow-lg transition duration-300 transform hover:scale-105">
                Pre-order Now
              </button>
              <button className="border-2 border-blue-600 text-blue-600 font-semibold py-3 px-8 rounded-lg hover:bg-blue-50 transition duration-300">
                Learn More
              </button>
            </div>
          </div>
          <div className="w-full md:w-1/2 md:pl-12"> {/* Added w-full for mobile */}
            <div className="bg-white p-4 rounded-xl shadow-xl">
              {/* Improved container with aspect ratio instead of fixed height */}
              <div className="relative aspect-video w-full overflow-hidden rounded-lg">
                <Image 
                  src={Eco}
                  alt="EcoCharge wireless charger" 
                  fill
                  className="object-cover"
                  sizes="(max-width: 768px) 100vw, 50vw"
                  priority
                />
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}