"use client"

import React from "react";

export function Pricing() {
    const plans = [
      {
        name: "Standard",
        description: "Perfect for everyday charging needs.",
        price: "$49.99",
        features: [
          "10W Charging",
          "Single Device",
          "1-Year Warranty"
        ],
        highlighted: false
      },
      {
        name: "Premium",
        description: "Enhanced charging for power users.",
        price: "$79.99",
        features: [
          "15W Fast Charging",
          "Dual Device Support",
          "3-Year Warranty",
          "Premium App Features"
        ],
        highlighted: true
      },
      {
        name: "Ultimate",
        description: "Maximum power for all your devices.",
        price: "$129.99",
        features: [
          "25W Turbo Charging",
          "Multi-Device (up to 4)",
          "Lifetime Warranty",
          "Priority Support"
        ],
        highlighted: false
      }
    ];
  
    return (
      <section id="pricing" className="py-16 bg-white">
        <div className="container mx-auto px-4 md:px-6">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-800 mb-4">Pricing Plans</h2>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto">
              Choose the perfect EcoCharge for your needs.
            </p>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {plans.map((plan, index) => (
              <div 
                key={index} 
                className={`${plan.highlighted 
                  ? 'bg-blue-50 border border-blue-200 transform scale-105 shadow-lg' 
                  : 'bg-white border border-gray-200 shadow-md'} 
                  rounded-xl p-8 hover:shadow-xl transition duration-300`}
              >
                {plan.highlighted && (
                  <div className="bg-blue-600 text-white text-sm font-bold px-4 py-1 rounded-full inline-block mb-4">MOST POPULAR</div>
                )}
                <h3 className="text-2xl font-bold text-gray-800 mb-4">{plan.name}</h3>
                <p className="text-gray-600 mb-6">{plan.description}</p>
                <div className="text-3xl font-bold text-blue-600 mb-6">{plan.price}</div>
                <ul className="space-y-3 mb-8">
                  {plan.features.map((feature, featureIndex) => (
                    <li key={featureIndex} className="flex items-center">
                      <svg className="w-5 h-5 text-green-500 mr-2" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                        <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd"></path>
                      </svg>
                      <span className="text-gray-600">{feature}</span>
                    </li>
                  ))}
                </ul>
                <button className="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-8 rounded-lg transition duration-300">
                  Select Plan
                </button>
              </div>
            ))}
          </div>
        </div>
      </section>
    );
  }