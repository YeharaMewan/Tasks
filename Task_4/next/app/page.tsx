// pages/index.js
import Head from 'next/head';

// Components
import {Navbar} from '../components/navbar';
import {Hero} from '../components/Hero';
import {Features} from '../components/Features';
import {HowItWorks} from '../components/HowItWorks';
import {CallToAction} from '../components/CallToAction';
import {Footer} from '../components/Footer';

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-b from-blue-50 to-white">
      <Head>
        <title>EcoCharge - Sustainable Wireless Charging</title>
        <meta name="description" content="Revolutionary eco-friendly wireless charging technology" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Navbar />
      <Hero />
      <Features />
      <HowItWorks />
      <CallToAction />
      <Footer />
    </div>
  );
}