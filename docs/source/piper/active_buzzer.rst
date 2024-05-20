.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

Active Buzzer
==================

In this project, we will learn how to use a button to control the active buzzer.

**Wring**

.. image:: img/doorbell.png

* An active buzzer is a device that makes a sound by directly giving high and low levels. Since the current coming out of the Pico pin is small, an NPN transistor is used here to amplify the current to make the buzzer sound louder.

* The 1K resistor between the NPN transistor and GP15 is used for current limiting when the transistor is energized.

**Code**

After connecting Pico, click the **Start** button and the code starts to run. The buzzer will sound when the button is pressed.

.. image:: img/pir.png
    :width: 300

.. note::
    This project code is exactly the same as the previous project :ref:`Button`.