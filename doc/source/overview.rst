Overview and Installation
=====

Rofunc package focuses on the **robotic Imitation Learning (IL) and Learning from Demonstration (LfD)** fields and provides valuable and 
convenient python functions for robotics, including _demonstration collection, data pre-processing, LfD algorithms, planning, and control methods. We also plan to provide an Isaac Gym-based robot simulator for evaluation. This package aims to advance the field by building a full-process toolkit and validation platform that simplifies and standardizes the process of demonstration data collection, processing, learning, and its deployment on robots.

.. image:: ../../img/pipeline.png


Installation
------------------

Install from PyPI
^^^^^^^^^^^^^^^^^^^^

**Requirements need to be installed manually**

1. pbdlib
2. Isaac Gym
3. ZED SDK

Then

.. code-block:: python

   pip install rofunc

Install from Source
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   git clone https://github.com/Skylark0924/Rofunc.git
   cd Rofunc
   pip install -r requirements.txt
   pip install -e .

.. note::

   Besides, you need to install `ZED SDK <https://www.stereolabs.com/developers/release/#downloads>`_ manually. (We have tried to package it as a :guilabel:`.whl` file to add it to :guilabel:`requirements.txt`, unfortunately, the ZED SDK is not very friendly and doesn't support direct installation.)


Available functions
------------------

+----------------------------------+---------------+--------------------------+-----------------------------------------------------------------------+
| Classes                          | Types         | Functions                | Description                                                           |
+==================================+===============+==========================+=======================================================================+
| **Devices**                      | Xsens         | `xsens.record`           | Record The Human Motion Via Network Streaming                         |
+----------------------------------+---------------+--------------------------+-----------------------------------------------------------------------+
|                                  |               | `xsens.process`          | Decode The .mvnx File                                                 |
+----------------------------------+---------------+--------------------------+-----------------------------------------------------------------------+
|                                  |               | `xsens.visualize`        | Show Or Save Gif About The Motion                                     |
+----------------------------------+---------------+--------------------------+-----------------------------------------------------------------------+
|                                  | Optitrack     | `optitrack.record`       | Record The Motion Of Markers Via Network Streaming                    |
+----------------------------------+---------------+--------------------------+-----------------------------------------------------------------------+
|                                  |               | `optitrack.process`      | Process The Output .csv Data                                          |
+----------------------------------+---------------+--------------------------+-----------------------------------------------------------------------+
|                                  |               | `optitrack.visualize`    | Show Or Save Gif About The Motion                                     |
+----------------------------------+---------------+--------------------------+-----------------------------------------------------------------------+
|                                  | ZED           | `zed.record`             | Record With Multiple Cameras                                          |
+----------------------------------+---------------+--------------------------+-----------------------------------------------------------------------+
|                                  |               | `zed.playback`           | Playback The Recording And Save Snapshots                             |
+----------------------------------+---------------+--------------------------+-----------------------------------------------------------------------+
|                                  |               | `zed.export`             | Export The Recording To Mp4                                           |
+----------------------------------+---------------+--------------------------+-----------------------------------------------------------------------+
|                                  | Multimodal    | `mmodal.record`          | Record Multi-Modal Demonstration Data Simultaneously                  |
+----------------------------------+---------------+--------------------------+-----------------------------------------------------------------------+
|                                  |               | `mmodal.export`          | Export Multi-Modal Demonstration Data In One Line                     |
+----------------------------------+---------------+--------------------------+-----------------------------------------------------------------------+
| **Learning From Demonstration**  | DMP           | `dmp.uni`                | DMP For One Agent With Several (or One) Demonstrated Trajectories     |
+----------------------------------+---------------+--------------------------+-----------------------------------------------------------------------+
|                                  | GMR           | `gmr.uni`                | GMR For One Agent With Several (or One) Demonstrated Trajectories     |
+----------------------------------+---------------+--------------------------+-----------------------------------------------------------------------+
|                                  | TP-GMM        | `tpgmm.uni`              | TP-GMM For One Agent With Several (or One) Demonstrated Trajectories  |
+----------------------------------+---------------+--------------------------+-----------------------------------------------------------------------+
|                                  |               | `tpgmm.bi`               | TP-GMM For Two Agent With Coordination Learned From Demonstration     |
+----------------------------------+---------------+--------------------------+-----------------------------------------------------------------------+
|                                  | TP-GMR        | `tpgmr.uni`              | TP-GMR For One Agent With Several (or One) Demonstrated Trajectories  |
+----------------------------------+---------------+--------------------------+-----------------------------------------------------------------------+
|                                  |               | `tpgmr.bi`               | TP-GMR For Two Agent With Coordination Learned From Demonstration     |
+----------------------------------+---------------+--------------------------+-----------------------------------------------------------------------+
| **Planning**                     | LQT           | `lqt.uni`                | LQT For One Agent With Several Via-Points                             |
+----------------------------------+---------------+--------------------------+-----------------------------------------------------------------------+
|                                  |               | `lqt.bi`                 | LQT For Two Agent With Coordination Constraints                       |
+----------------------------------+---------------+--------------------------+-----------------------------------------------------------------------+
|                                  |               | `lqt.recursive`          | Generate Smooth Trajectories For Robot Execution Recursively          |
+----------------------------------+---------------+--------------------------+-----------------------------------------------------------------------+
| **Logger**                       |               | `logger.write`           | Custom Tensorboard-Based Logger                                       |
+----------------------------------+---------------+--------------------------+-----------------------------------------------------------------------+
| **Coordinate**                   |               | `coord.custom_class`     | Define The Custom Class Of `Pose`                                     |
+----------------------------------+---------------+--------------------------+-----------------------------------------------------------------------+
|                                  |               | `coord.transform`        | Useful Functions About Coordinate Transformation                      |
+----------------------------------+---------------+--------------------------+-----------------------------------------------------------------------+
| **VisuaLab**                     | Trajectory    | `visualab.trajectory`    | 2-Dim/3-Dim/with Ori Trajectory Visualization                         |
+----------------------------------+---------------+--------------------------+-----------------------------------------------------------------------+
|                                  | Distribution  | `visualab.distribution`  | 2-Dim/3-Dim Distribution Visualization                                |
+----------------------------------+---------------+--------------------------+-----------------------------------------------------------------------+
|                                  | Ellipsoid     | `visualab.ellipsoid`     | 2-Dim/3-Dim Ellipsoid Visualization                                   |
+----------------------------------+---------------+--------------------------+-----------------------------------------------------------------------+
| **RoboLab**                      | Kinematics    | `robolab.kinematics`     | ...                                                                   |
+----------------------------------+---------------+--------------------------+-----------------------------------------------------------------------+































