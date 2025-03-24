"use client"

import React from "react";

export function HowItWorks() {
  const steps = [
    {
      number: "1",
      title: "Place",
      description: "Place your device on the EcoCharge pad."
    },
    {
      number: "2",
      title: "Align",
      description: "Auto-alignment technology positions your device perfectly."
    },
    {
      number: "3",
      title: "Charge",
      description: "Efficient charging begins automatically."
    },
    {
      number: "4",
      title: "Monitor",
      description: "Track charging progress with the companion app."
    }
  ];

  return (
    <section id="how-it-works" className="py-16 bg-gray-50">
      <div className="container mx-auto px-4 md:px-6">
        <div className="text-center mb-16">
          <h2 className="text-3xl md:text-4xl font-bold text-gray-800 mb-4">How It Works</h2>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            Simple, sustainable, and efficient wireless charging.
          </p>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          {steps.map((step, index) => (
            <div key={index} className="text-center">
              <div className="bg-blue-100 rounded-full w-16 h-16 flex items-center justify-center mb-6 mx-auto">
                <span className="text-blue-600 font-bold text-xl">{step.number}</span>
              </div>
              <h3 className="text-lg font-bold text-gray-800 mb-3">{step.title}</h3>
              <p className="text-gray-600">
                {step.description}
              </p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}