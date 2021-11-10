package com.example.ortua_app

import android.os.Bundle
import android.view.*
import androidx.fragment.app.Fragment
import androidx.databinding.DataBindingUtil
import androidx.navigation.findNavController
import androidx.navigation.ui.NavigationUI
import com.example.ortua_app.databinding.FragmentHomeBinding


class HomeFragment : Fragment() {

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        val binding = DataBindingUtil.inflate<FragmentHomeBinding>(
            inflater,R.layout.fragment_home, container, false)

        binding.btnProceed.setOnClickListener { view : View ->

            when (binding.userOptions.checkedRadioButtonId){
                R.id.option_bg -> view.findNavController().navigate(R.id.action_homeFragment_to_backgroundFragment)
                R.id.option_par -> view.findNavController().navigate(R.id.action_homeFragment_to_parametersFragment)
                else -> view.findNavController().navigate(R.id.action_homeFragment_to_notificationsFragment)
            }
        }
        setHasOptionsMenu(true)
        return binding.root

    }

    override fun onCreateOptionsMenu(menu: Menu, inflater: MenuInflater) {
        super.onCreateOptionsMenu(menu, inflater)
        inflater.inflate(R.menu.options_menu, menu)
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        return NavigationUI.onNavDestinationSelected(item,requireView().findNavController()) || super.onOptionsItemSelected(item)
    }

}