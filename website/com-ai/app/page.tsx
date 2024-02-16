"use client";
import React from 'react';
import CommueGifImage from '@/public/git/logo/CubesShufflingGIF.gif'
import Image from 'next/image';
import { Dropdown, Modal, Space, Select } from 'antd';

const words: string[] = ["developers.", "designers.", "creators.", "everyone.", "<END>"];
const colour: string[] = ["text-[#00000]", "text-[#ffb4ed] dark:text-[#FFD6F5]", "text-[#FF8F8F]  dark:text-[#FF8F8F]", "text-[#ffef40] dark:text-[#FFF7A1]"];

const TITLE = "Commune AI Model";
const TAGLINE = "World's largest Model for ";

export default function HomepageHeader() {

  // blinker
  const [index, setIndex] = React.useState(0);
  const [subIndex, setSubIndex] = React.useState(0);
  const [blink, setBlink] = React.useState(true);
  const [reverse, setReverse] = React.useState(false);

  //modal flag
  const [isShowGetImageModalOpen, setIsShowGetImageModalOpen] = React.useState(false)
  const [isShowGetTextModalOpen, setIsShowGetTextModalOpen] = React.useState(false)
  const [isShowGetVideoModalOpen, setIsShowGetVideoModalOpen] = React.useState(false)
  // state of the scroll position and header height
  const [scrollPosition, setScrollPosition] = React.useState(0);
  const headerRef = React.useRef<any>(null);
  const [headerHeight, setHeaderHeight] = React.useState(20);

  // typeWriter effect
  // give me the context of this whole useEffect
  React.useEffect(() => {
    if (index === words.length) return; // if end of words, return
    // if subIndex is equal to the length of the word + 1 and index is not the last word and not reverse
    if (subIndex === words[index].length + 1 && index !== words.length - 1 && !reverse) {
      setReverse(true);
      return;
    }
    // if subIndex is equal to 0 and reverse is true
    if (subIndex === 0 && reverse) {
      setReverse(false);
      setIndex((prev) => prev + 1);
      return;
    }
    // if reverse is true, subIndex is not 0 and index is not the last word
    if (index === words.length - 1)
      setIndex(() => 0)
    // if reverse is true, subIndex is not 0 and index is not the last word
    // if reverse is false, subIndex is not the length of the word and index is not the last word
    const timeout = setTimeout(() => {
      setSubIndex((prev) => prev + (reverse ? -1 : 1));
    }, Math.max(reverse ? 75 : subIndex === words[index].length ? 1000 :
      75, 25));
    return () => clearTimeout(timeout);
  }, [subIndex, index, reverse]);


  // blinker effect
  React.useEffect(() => {
    const timeout2 = setTimeout(() => {
      setBlink((prev) => !prev);
    }, 250);
    if (index === words.length) return;

    return () => clearTimeout(timeout2);
  }, [blink]);

  // Handle scroll position
  const handleScroll = () => {
    const position = window.pageYOffset;
    setScrollPosition(position);
  };

  // Add scroll event listener to window
  React.useEffect(() => {
    window.addEventListener('scroll', handleScroll, { passive: true });

    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  }, []);

  // Get header height on mount and when window is resized
  // This is to offset the scroll position so that the header

  const handleShowGetImageModal = () => {
    setIsShowGetImageModalOpen(true)
  }

  const handleShowGetImageModalCancel = () => {
    setIsShowGetImageModalOpen(false)
  }

  const handleShowGetTextModal = () => {
    setIsShowGetTextModalOpen(true)
  }

  const handleShowGetTextModalCancel = () => {
    setIsShowGetTextModalOpen(false)
  }

  const handleShowGetVideoModal = () => {
    setIsShowGetVideoModalOpen(true)
  }

  const handleShowGetVideoModalCancel = () => {
    setIsShowGetVideoModalOpen(false)
  }

  return (
    <header ref={headerRef} className={` dark:bg-[#161616] p-[4rem] py-32 text-center overflow-hidden ${getHeaderClasses(scrollPosition, headerHeight)} duration-500`} >

      <Image src={CommueGifImage} alt="Commune Logo" className='block sm:hidden' />
      <div className="px-10 py-5">
        <div className='flex lg:flex-row flex-col h-1/2'>
          <div className='w-full lg:w-1/2 flex flex-col items-center justify-center'>

            <div className=' w-auto sm:w-[710px] sm:h-[250px] '>
              <h1 className=" text-4xl sm:text-6xl sm:pb-3 dark:text-white">{TITLE}</h1>
              <div className='hidden sm:block'>
                <p className="hero__subtitle text-xl sm:text-4xl">{TAGLINE}
                  <br />
                  <span className={`hero__subtitle text-4xl ${colour[index]} font-semibold mb-5`}>{`${words[index].substring(0, subIndex)}${blink ? "|" : ""}`}</span></p>
              </div>
            </div>

            <div className='flex w-full items-center justify-evenly'>
              <div className=' bg-blue-700 rounded-lg shadow-lg hover:shadow-2xl text-center hover:bg-blue-600 duration-200 text-white hover:text-white font-sans font-semibold justify-center px-2 py-2 hover:border-blue-300 hover:border-2 hover:border-solid cursor-pointer' onClick={handleShowGetImageModal}>
                🎴 Get the Image
              </div>
              <div className=' bg-blue-700 rounded-lg shadow-lg hover:shadow-2xl text-center hover:bg-blue-600 duration-200 text-white hover:text-white font-sans font-semibold justify-center px-2 py-2 hover:border-blue-300 hover:border-2 hover:border-solid cursor-pointer' onClick={handleShowGetTextModal}>
                📝 Get the Text
              </div>
              <div className=' bg-blue-700 rounded-lg shadow-lg hover:shadow-2xl text-center hover:bg-blue-600 duration-200 text-white hover:text-white font-sans font-semibold justify-center px-2 py-2 hover:border-blue-300 hover:border-2 hover:border-solid cursor-pointer' onClick={handleShowGetVideoModal}>
                🎥 Get the Video
              </div>
            </div>

          </div>

          <div className='w-full lg:w-[75%] h-full lg:-mr-44 '>
            <Image src={CommueGifImage} alt="Commune Logo" className='visible' style={{ visibility: 'visible' }} />
          </div>

        </div>
      </div>
      {
        isShowGetImageModalOpen
        &&
        <Modal open={isShowGetImageModalOpen} onCancel={handleShowGetImageModalCancel} footer={null} >
          <div className="flex flex-col">


          </div>
        </Modal>
      }
    </header>
  );
}

export const getHeaderClasses = (position: number, height: number) => {
  if (position > (height / 2)) {
    return 'rounded-b-lg shadow-lg mx-5';
  }
  return '';
}
