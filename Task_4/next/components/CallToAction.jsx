"use client"

import React from "react";

import { useRouter } from 'next/navigation';

export function CallToAction() {

  const router = useRouter();
  
    const handlePreOrder = () =>{
    router.push('/Plan')
  }
  
  return (
    <section className="py-20 bg-blue-600">
      <div className="container mx-auto px-4 md:px-6 text-center">
        <h2 className="text-3xl md:text-4xl font-bold text-white mb-6">Ready to Make the Switch?</h2>
        <p className="text-xl text-blue-100 mb-8 max-w-3xl mx-auto">
          Join thousands of environmentally conscious consumers who are charging smarter with EcoCharge.
        </p>
        <div className="flex flex-col sm:flex-row gap-4 justify-center">
          <button
            onClick={handlePreOrder}
            className="bg-white hover:bg-blue-50 text-blue-600 font-semibold py-3 px-8 rounded-lg shadow-lg transition duration-300 transform hover:scale-105">
            Pre-order Now
          </button>
          <button className="border-2 border-white text-white hover:bg-blue-500 font-semibold py-3 px-8 rounded-lg transition duration-300">
            Contact Sales
          </button>
        </div>
      </div>
    </section>
  );
}
